"""Модуль сверки. Выданная программа, править нельзя.

Содержимого памяти он не помнит — только правила, по которым она была
устроена, и контрольные суммы. Поэтому скажет «сошлось» или «не сошлось»
и ни слова о том, где именно.

Как пользоваться:

    python3 src/partner/verify.py src/main.py
        Проверить всё, что уже сделано. Незаконченные задания отмечаются
        как «не реализовано» и зачёт остальным не портят.

    python3 src/partner/verify.py src/main.py --task 5
        Проверить одно задание.

    python3 src/partner/verify.py --control
        Породить контрольный файл. Печатает ключ и три случайные строки.

    python3 src/partner/verify.py --control КЛЮЧ src/main.py
        Прогон на контрольном файле с этим ключом.

    python3 src/partner/verify.py --restored src/restore.py
        Проверить восстановитель из бонусного задания.
"""

import os
import random
import subprocess
import sys
import tempfile

TIMEOUT = 20
PUBLIC = os.path.join("datasets", "memory.log")
REASONS = ["пустая строка", "неверное число полей", "пустое имя модуля",
           "неверное время", "пустое значение", "значение не число"]

# ---------------------------------------------------------------- разбор


def is_time(text):
    parts = text.split(":")
    if len(parts) != 3:
        return False
    for part, top in zip(parts, (23, 59, 59)):
        if len(part) != 2 or not part.isdigit() or not part.isascii():
            return False
        if int(part) > top:
            return False
    return True


def is_number(text):
    body = text[1:] if text[:1] in "+-" else text
    if body.count(".") > 1:
        return False
    if body.endswith("."):
        return False
    digits = body.replace(".", "")
    return len(digits) > 0 and digits.isdigit() and digits.isascii()


def classify(line):
    """Возвращает (причина или None, имя или None, значение или None)."""
    if line.strip() == "":
        return "пустая строка", None, None
    fields = [f.strip() for f in line.split(";")]
    if len(fields) != 3:
        return "неверное число полей", None, None
    moment, name, value = fields
    if name == "":
        return "пустое имя модуля", None, None
    if not is_time(moment):
        return "неверное время", name, None
    if value == "":
        return "пустое значение", name, None
    if not is_number(value):
        return "значение не число", name, None
    return None, name, float(value)


def read_lines(text):
    lines = text.split("\n")
    if lines and lines[-1] == "":
        lines.pop()
    return lines


# ------------------------------------------------------------- эталоны


def scan_expected(text, axis_a):
    lines = read_lines(text)
    parsed = 0
    display = {}
    counts = {}
    for line in lines:
        reason, name, _ = classify(line)
        if reason != "неверное число полей" and reason != "пустая строка":
            parsed += 1
        if name is None:
            continue
        key = name.lower() if axis_a else name
        display.setdefault(key, name)
        counts[key] = counts.get(key, 0) + 1
    order = sorted(counts, key=lambda k: (-counts[k], display[k]))
    out = ["%d %d %d" % (len(lines), parsed, len(lines) - parsed)]
    out += ["%s %d" % (display[k], counts[k]) for k in order]
    return "\n".join(out)


def reasons_expected(text):
    counts = {}
    for line in read_lines(text):
        reason, _, _ = classify(line)
        if reason is not None:
            counts[reason] = counts.get(reason, 0) + 1
    order = sorted(counts, key=lambda r: (-counts[r], REASONS.index(r)))
    return "\n".join("%s %d" % (r, counts[r]) for r in order)


def report_expected(text, axis_a, axis_b):
    lines = read_lines(text)
    display, values, seen = {}, {}, {}
    accepted = 0
    for line in lines:
        reason, name, value = classify(line)
        if name is not None:
            key = name.lower() if axis_a else name
            display.setdefault(key, name)
            seen.setdefault(key, True)
            values.setdefault(key, [])
        if reason is None:
            values[name.lower() if axis_a else name].append(value)
            accepted += 1
    rows = []
    for key in sorted(seen, key=lambda k: display[k]):
        got = values[key]
        if not got and not axis_b:
            continue
        if got:
            average = "%.3f" % (sum(got) / len(got))
            if float(average) == 0.0:
                average = "0.000"
        else:
            average = "-"
        rows.append("%s | %d | %s" % (display[key], len(got), average))
    rows.append("ИТОГО | %d | %d" % (accepted, len(lines) - accepted))
    return "\n".join(rows)


def restore_expected(text):
    out, restored, dropped = [], 0, 0
    for line in read_lines(text):
        reason, _, _ = classify(line)
        if reason is None:
            out.append(line)
            continue
        fixed = try_restore(line)
        if fixed is None:
            dropped += 1
        else:
            out.append(fixed)
            restored += 1
    return "\n".join(out), "восстановлено %d\nвыброшено %d" % (restored, dropped)


def try_restore(line):
    if line.strip() == "":
        return None
    fields = [f.strip() for f in line.split(";")]
    if len(fields) != 3 or fields[1] == "":
        return None
    moment, name, value = fields
    if not is_time(moment):
        parts = moment.split(":")
        if len(parts) != 3:
            return None
        fixed = []
        for part, top in zip(parts, (23, 59, 59)):
            if not (1 <= len(part) <= 2) or not part.isdigit() or not part.isascii():
                return None
            if int(part) > top:
                return None
            fixed.append("%02d" % int(part))
        moment = ":".join(fixed)
    if value == "":
        return None
    if not is_number(value):
        value = value.replace(",", ".")
        if not is_number(value):
            return None
    return "%s;%s;%s" % (moment, name, value)


# ------------------------------------------------------------ фрагменты

def fragment(kind, key):
    """Фрагменты для проверки заданий."""
    rnd = random.Random(key)
    lines = []

    def good(name, value):
        lines.append("%02d:%02d:%02d;%s;%s" % (rnd.randrange(24), rnd.randrange(60),
                                               rnd.randrange(60), name, value))

    def bad(name):
        lines.append("%02d:%02d:%02d;%s;%s" % (rnd.randrange(24), rnd.randrange(60),
                                               rnd.randrange(60), name, "1e3"))

    if kind in ("a", "ab"):
        for _ in range(3):
            bad("RADIO")
    if kind in ("b", "ab"):
        for value in ("10.0", "20.0"):
            good("SENSOR", value)
        for value in ("30.0", "40.0"):
            good("sensor", value)
    for value in ("1.0", "2.0", "3.5"):
        good("POWER", value)
    lines.append("")
    lines.append("12:00:00;VALVE")
    lines.append("12:00:01;;7.0")
    lines.append("9:1:1;VALVE;5.0")
    lines.append("12:00:02;VALVE;")
    good("VALVE", "8.25")
    rnd.shuffle(lines)
    return "\n".join(lines) + "\n"


# --------------------------------------------------------------- запуск

def run(program, path, extra=()):
    command = [sys.executable, program, path] + list(extra)
    try:
        done = subprocess.run(command, capture_output=True, text=True, timeout=TIMEOUT)
    except subprocess.TimeoutExpired:
        return None, None, "таймаут"
    return done.stdout.rstrip("\n"), done.stderr.rstrip("\n"), done.returncode


def write_temp(text, folder, name):
    path = os.path.join(folder, name)
    with open(path, "w", encoding="utf-8") as target:
        target.write(text)
    return path


def status(ok, empty):
    if empty:
        return "не реализовано"
    return "сошлось" if ok else "не сошлось"


def variants_report(text):
    """Все допустимые варианты отчёта."""
    return {(axis_a, axis_b): report_expected(text, axis_a, axis_b)
            for axis_a in (False, True) for axis_b in (False, True)}


def which_variant(text, produced):
    for axes, expected in variants_report(text).items():
        if produced == expected:
            return axes
    return None


# --------------------------------------------------------------- задания

def check_scan(program, folder):
    text = fragment("ab", 11)
    path = write_temp(text, folder, "scan.log")
    out, _, code = run(program, path, ["--scan"])
    if out is None or out == "" or code != 0:
        return "не реализовано", "не реализовано"
    first_ok = out.split("\n")[0] == scan_expected(text, False).split("\n")[0]
    whole_ok = out in (scan_expected(text, False), scan_expected(text, True))
    return status(first_ok, False), status(whole_ok, False)


def check_reasons(program, folder):
    text = fragment("ab", 12)
    path = write_temp(text, folder, "reasons.log")
    out, err, code = run(program, path)
    if err is None or err == "":
        return "не реализовано"
    return status(err == reasons_expected(text), False)


def check_report(program, folder):
    text = fragment("ab", 13)
    path = write_temp(text, folder, "report.log")
    out, _, code = run(program, path)
    if out is None or out == "" or code != 0:
        return "не реализовано"
    if which_variant(text, out) is None:
        return "не сошлось"
    if os.path.isfile(os.path.join("src", "report.txt")):
        public_out, _, _ = run(program, PUBLIC)
        with open(os.path.join("src", "report.txt"), encoding="utf-8") as saved:
            if saved.read().rstrip("\n") != (public_out or ""):
                return "не сошлось: сохранённый отчёт не совпадает с программой"
    return "сошлось"


def check_forks(program, folder):
    text = fragment("ab", 14)
    path = write_temp(text, folder, "forks.log")
    base, _, code = run(program, path)
    if base is None or base == "" or code != 0:
        return "не реализовано"
    first, _, code_one = run(program, path, ["--alt", "1"])
    second, _, code_two = run(program, path, ["--alt", "2"])
    if not first or not second or code_one != 0 or code_two != 0:
        return "не реализовано"
    axes_base = which_variant(text, base)
    axes_one = which_variant(text, first)
    axes_two = which_variant(text, second)
    if None in (axes_base, axes_one, axes_two):
        return "не сошлось"
    moved_one = [i for i in (0, 1) if axes_one[i] != axes_base[i]]
    moved_two = [i for i in (0, 1) if axes_two[i] != axes_base[i]]
    if len(moved_one) != 1 or len(moved_two) != 1 or moved_one == moved_two:
        return "не сошлось"
    return "сошлось"


def check_restore(program, folder):
    text = fragment("ab", 15)
    path = write_temp(text, folder, "restore.log")
    out, err, code = run(program, path)
    if out is None or out == "" or code != 0:
        return "не реализовано"
    body, counters = restore_expected(text)
    if out != body:
        return "не сошлось"
    if (err or "") != counters:
        return "не сошлось: счётчики"
    return "сошлось"


# ------------------------------------------------------------------ вывод

def report(pairs):
    for name, value in pairs:
        print("%-28s %s" % (name, value))
    return 0 if all(v.startswith("сошлось") or v == "не реализовано"
                    for _, v in pairs) else 1


def self_check(program, only):
    if not os.path.isfile(program):
        print("Файл не найден: " + program)
        return 1
    with tempfile.TemporaryDirectory() as folder:
        first, second = check_scan(program, folder)
        pairs = [
            ("задание 1  разведка", first),
            ("задание 2  модули", second),
            ("задание 4  отбраковка", check_reasons(program, folder)),
            ("задание 5  отчёт", check_report(program, folder)),
            ("задание 6  развилки", check_forks(program, folder)),
        ]
    if only is not None:
        pairs = [p for p in pairs if p[0].startswith("задание %d" % only)]
        if not pairs:
            print("Такого задания модуль сверки не проверяет.")
            return 1
    code = report(pairs)
    if only is None and all(value == "сошлось" for _, value in pairs):
        print("одному такое не поднять")
    return code


def control_new():
    sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__))))
    key = random.randrange(1000, 9999)
    text = make_control(key)
    name = "control_%d.log" % key
    with open(name, "w", encoding="utf-8") as target:
        target.write(text)
    lines = [l for l in read_lines(text) if l.strip() != ""]
    picked = random.Random(key).sample(lines, 3)
    print("Ключ: %d" % key)
    print("Файл: %s" % name)
    print("")
    print("Три строки для предсказания:")
    for line in picked:
        print("    " + line)
    print("")
    print("Дальше: python3 src/partner/verify.py --control %d <программа>" % key)
    return 0


def make_control(key):
    rnd = random.Random(key * 7919)
    names = ["SENSOR", "sensor", "POWER", "RADIO", "VALVE", "Pump_1"]
    lines, seen = [], set()

    def add(line):
        if line.strip() == "":
            lines.append(line)
            return True
        if line in seen:
            return False
        seen.add(line)
        lines.append(line)
        return True

    def moment():
        return "%02d:%02d:%02d" % (rnd.randrange(24), rnd.randrange(60), rnd.randrange(60))

    for _ in range(4):
        add("%s;RADIO;%s" % (moment(), rnd.choice(["1e3", "nan", "7,5", ""])))
    for _ in range(3):
        add("")
        add("%s;%s" % (moment(), rnd.choice(names)))
        add("%s;;%.1f" % (moment(), rnd.uniform(0, 50)))
        add("%d:%d:%d;%s;%.1f" % (rnd.randrange(10), rnd.randrange(10),
                                  rnd.randrange(10), rnd.choice(names), rnd.uniform(0, 50)))
    while len(lines) < 200:
        name = rnd.choice([n for n in names if n != "RADIO"])
        if rnd.random() < 0.2:
            add("%s;%s;%s" % (moment(), name, rnd.choice(["1e3", "abc", "3,5"])))
        else:
            add("%s;%s;%.1f" % (moment(), name, rnd.uniform(-40, 120)))
    rnd.shuffle(lines)
    return "\n".join(lines) + "\n"


def control_run(key, program):
    name = "control_%d.log" % key
    if not os.path.isfile(name):
        with open(name, "w", encoding="utf-8") as target:
            target.write(make_control(key))
    text = open(name, encoding="utf-8").read()
    out, err, code = run(program, name)
    if out is None:
        print("Программа не завершилась.")
        return 1
    pairs = [
        ("отчёт", status(which_variant(text, out) is not None, out == "")),
        ("причины отбраковки", status((err or "") == reasons_expected(text), not err)),
    ]
    scan_out, _, _ = run(program, name, ["--scan"])
    pairs.append(("разведка", status(
        scan_out in (scan_expected(text, False), scan_expected(text, True)),
        not scan_out)))
    return report(pairs)


def main():
    args = sys.argv[1:]
    if not args:
        print(__doc__)
        return 1
    if args[0] == "--control":
        rest = args[1:]
        if not rest:
            return control_new()
        if len(rest) == 2 and rest[0].isdigit():
            return control_run(int(rest[0]), rest[1])
        print("Нужно: --control  либо  --control КЛЮЧ ПРОГРАММА")
        return 1
    if args[0] == "--restored":
        if len(args) != 2:
            print("Нужно: --restored ПРОГРАММА")
            return 1
        with tempfile.TemporaryDirectory() as folder:
            return report([("задание 7  восстановление",
                            check_restore(args[1], folder))])
    only = None
    program = args[0]
    if "--task" in args:
        index = args.index("--task")
        if index + 1 >= len(args) or not args[index + 1].isdigit():
            print("Нужно: --task НОМЕР")
            return 1
        only = int(args[index + 1])
    return self_check(program, only)


sys.exit(main())
