#!/usr/bin/env python3
"""Локальная выдача, перенос и наблюдения для пира. Оценок не выставляет.

Запускайте этот файл из отдельной чистой копии выданного комплекта.
Python 3.8+, Git, Bash; только стандартная библиотека, без сети.
"""
import argparse
import hashlib
import json
import os
from pathlib import Path
import random
import shutil
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
BASE_TAG = "day01-start"
REQUIRED = {"src/partner/memory.txt", "src/quest1.sh", "src/hello.py",
            "src/calc.py", "src/signal.py", "src/errors.md", "src/HOWTO.md"}
OPTIONAL = {"src/quest6.sh"}


def command(args, cwd, data=None, limit=15):
    return subprocess.run([str(a) for a in args], cwd=str(cwd), input=data,
                          stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                          timeout=limit)


def git(cwd, *args):
    result = command(["git", *args], cwd)
    if result.returncode:
        raise ValueError(result.stderr.decode("utf-8", "replace").strip())
    return result.stdout.decode("utf-8", "replace").strip()


def write_json(path, value):
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def files(root):
    return {p.relative_to(root).as_posix(): p for p in root.rglob("*")
            if p.is_file() and not any(x in {".git", "__pycache__", ".day01"}
                                       for x in p.relative_to(root).parts)}


def readiness():
    if sys.version_info < (3, 8):
        raise ValueError("Нужен Python 3.8 или новее.")
    for name in ["git", "bash"]:
        if not shutil.which(name):
            raise ValueError("Не установлена обязательная программа: " + name)


def start(args):
    readiness()
    if (ROOT / ".git").exists():
        raise ValueError("Репозиторий уже начат. Повторная выдача не требуется.")
    # Существующую Git-историю не перезаписываем. Личность задаётся только локально.
    git(ROOT, "init")
    git(ROOT, "symbolic-ref", "HEAD", "refs/heads/main")
    git(ROOT, "config", "user.name", args.name)
    git(ROOT, "config", "user.email", args.email)
    git(ROOT, "config", "commit.gpgsign", "false")
    git(ROOT, "config", "core.autocrlf", "false")
    git(ROOT, "add", ".")
    git(ROOT, "commit", "-m", "Day 01: исходный комплект")
    git(ROOT, "tag", BASE_TAG)
    git(ROOT, "checkout", "-b", "develop")
    print("Выдача завершена: исходный коммит, метка day01-start, ветка develop.")
    print("Открой README.md. Все задания уже доступны; кодов разблокировки нет.")


def check_tree(repo, revision, require_results=True):
    trusted = files(ROOT)
    tracked = set(git(repo, "ls-tree", "-r", "--name-only", revision).splitlines())
    allowed = set(trusted) | REQUIRED | OPTIONAL
    issues = ["Лишний отслеживаемый файл: " + n for n in sorted(tracked - allowed)]
    if require_results:
        issues += ["Не сдан файл: " + n for n in sorted(REQUIRED - tracked)]
    for name, path in trusted.items():
        if name == "src/partner/memory.txt" and require_results:
            continue
        result = command(["git", "show", revision + ":" + name], repo)
        if result.returncode or result.stdout != path.read_bytes():
            issues.append("Исходный файл отсутствует или изменён: " + name)
    return issues


def pack(args):
    repo = ROOT
    if git(repo, "branch", "--show-current") != "develop":
        raise ValueError("Перед сдачей переключись на develop.")
    if git(repo, "status", "--porcelain", "--untracked-files=all"):
        raise ValueError("Есть незакоммиченные или лишние файлы. Проверь git status.")
    feature_exists = command(["git", "rev-parse", "--verify", "feature/first-scripts"], repo).returncode == 0
    git(repo, "merge-base", "--is-ancestor", BASE_TAG, "develop")
    out = Path(args.out).resolve()
    if out == repo or repo in out.parents:
        raise ValueError("Каталог сдачи должен находиться вне репозитория.")
    out.mkdir(parents=True, exist_ok=False)
    bundle = out / "submission.bundle"
    refs = ["develop", BASE_TAG] + (["feature/first-scripts"] if feature_exists else [])
    git(repo, "bundle", "create", str(bundle), *refs)
    metadata = {"format": 1, "commit": git(repo, "rev-parse", "develop"),
                "base": git(repo, "rev-parse", BASE_TAG),
                "bundle_sha256": hashlib.sha256(bundle.read_bytes()).hexdigest()}
    write_json(out / "submission.json", metadata)
    print("Сданная версия: " + metadata["commit"])
    print("Передай пиру каталог целиком: " + str(out))
    print("После передачи эта версия заморожена. Заметки вечера храни отдельно.")
    if not feature_exists:
        print("Feature-ветки нет: неполная работа передаётся, отсутствие отметит пир.")


def intake(args):
    readiness()
    source = Path(args.submission).resolve()
    out = Path(args.out).resolve()
    meta = json.loads((source / "submission.json").read_text(encoding="utf-8"))
    bundle = source / "submission.bundle"
    if hashlib.sha256(bundle.read_bytes()).hexdigest() != meta["bundle_sha256"]:
        raise ValueError("Контрольная сумма bundle не совпадает; нужна исходная переданная копия.")
    out.mkdir(parents=True, exist_ok=False)
    repo = out / "submitted"
    git(out, "clone", "--branch", "develop", str(bundle), str(repo))
    head = git(repo, "rev-parse", "HEAD")
    if head != meta["commit"] or git(repo, "rev-parse", BASE_TAG) != meta["base"]:
        raise ValueError("Версия или стартовая метка не совпадают с карточкой сдачи.")
    issues = check_tree(repo, BASE_TAG, False) + check_tree(repo, head)
    # Неизменность проверяется по всей истории участника, включая изменения с откатом.
    protected = sorted(set(files(ROOT)) - {"src/partner/memory.txt"})
    changes = git(repo, "log", "--format=%h %s", BASE_TAG + ".." + head, "--", *protected)
    if changes:
        issues.append("В истории участника менялись исходные файлы:\n" + changes)
    all_changes = set(git(repo, "log", "--format=", "--name-only", BASE_TAG + ".." + head).splitlines())
    forbidden = all_changes - REQUIRED - OPTIONAL - {""}
    if forbidden:
        issues.append("В истории есть изменения вне результатов: " + ", ".join(sorted(forbidden)))
    write_json(out / "receipt.json", meta)
    write_json(out / "integrity.json", {"issues": issues})
    print("Приём зафиксирован: " + head)
    print("Проверка исходного комплекта: " + ("совпадает" if not issues else "есть расхождения"))
    for issue in issues:
        print("- " + issue)
    print("Пир читает исходники и расхождения, затем запускает verify. Оценку выставляет только пир.")


def run_case(repo, script, data, expected):
    try:
        result = command([sys.executable, repo / "src" / script], repo,
                         data.encode("utf-8"), limit=3)
        actual = result.stdout.decode("utf-8", "replace")
        return {"script": script, "input": data, "expected": expected,
                "stdout": actual, "stderr": result.stderr.decode("utf-8", "replace"),
                "exit": result.returncode,
                "matches": result.returncode == 0 and actual == expected and not result.stderr}
    except subprocess.TimeoutExpired:
        return {"script": script, "input": data, "expected": expected,
                "matches": False, "timeout": True}


def verify(args):
    review = Path(args.review).resolve()
    repo = review / "submitted"
    meta = json.loads((review / "receipt.json").read_text(encoding="utf-8"))
    if git(repo, "rev-parse", "HEAD") != meta["commit"] or git(repo, "status", "--porcelain"):
        raise ValueError("Сданная копия изменена. Создай новый каталог intake из исходного bundle.")
    cases = json.loads((ROOT / "datasets/cases.json").read_text(encoding="utf-8"))
    rows = [run_case(repo, c["script"], c["input"], c["output"]) for c in cases]
    boot = command([sys.executable, "src/partner/boot.py"], repo)
    branch = "origin/feature/first-scripts"
    history = {"personal_commits": int(git(repo, "rev-list", "--count", BASE_TAG + "..develop")),
               "graph": git(repo, "log", "--graph", "--oneline", "--all", BASE_TAG + "..develop")}
    exists = command(["git", "rev-parse", "--verify", branch], repo).returncode == 0
    feature = git(repo, "log", "--no-merges", "--format=%H\t%s", BASE_TAG + ".." + branch).splitlines() if exists else []
    history["feature_exists"] = exists
    history["feature_merged"] = exists and command(["git", "merge-base", "--is-ancestor", branch, "develop"], repo).returncode == 0
    history["feature_commits"] = feature
    history["feature_prefixed"] = sum(x.split("\t", 1)[1].startswith("feature/first-scripts:") for x in feature)
    history["merges"] = git(repo, "rev-list", "--min-parents=2", BASE_TAG + "..develop").splitlines()
    bonus = None
    if (repo / "src/quest6.sh").is_file():
        result = command(["bash", "src/quest6.sh"], repo)
        phrase = "".join(chr(int(x, 16)) for x in (ROOT / "src/partner/dump.txt").read_text().split())
        remaining = list((repo / "dump").iterdir()) if (repo / "dump").is_dir() else []
        bonus = {"exit": result.returncode, "stdout": result.stdout.decode("utf-8", "replace"),
                 "stderr": result.stderr.decode("utf-8", "replace"),
                 "matches": result.returncode == 0 and result.stdout.decode("utf-8", "replace").splitlines()[-1:] == [phrase]
                 and len(remaining) == len(phrase) and all(p.is_file() and p.name.startswith("part") and p.suffix == ".frag" for p in remaining)}
    evidence = {"commit": meta["commit"], "cases": rows, "history": history, "bonus": bonus,
                "boot": {"exit": boot.returncode, "stdout": boot.stdout.decode("utf-8", "replace"),
                         "matches": boot.returncode == 0 and b"5" in boot.stdout}}
    write_json(review / "evidence.json", evidence)
    print("Совпадений вход/выход: %d/%d" % (sum(r["matches"] for r in rows), len(rows)))
    for row in rows:
        if not row["matches"]:
            print("Расхождение: " + row["script"] + " " + repr(row["input"]))
    print("Коммитов участника: " + str(history["personal_commits"]))
    print("Наблюдения сохранены в evidence.json. Это не оценка и не зачёт.")


def card(args):
    review = Path(args.review).resolve()
    number = args.part
    path = review / ("card%d.json" % number)
    if path.exists():
        print(path.read_text(encoding="utf-8"))
        return
    rng = random.SystemRandom()
    token = "".join(rng.choice("abcdefghjkmnpqrstuvwxyz") for _ in range(6))
    target = review / ("practice%d" % number)
    if target.exists():
        raise ValueError("Папка практики уже есть, а карточки нет. Используй новый каталог проверки.")
    git(review, "clone", "--branch", "develop", str(review / "submitted"), str(target))
    git(target, "config", "user.name", "Day01 practice")
    git(target, "config", "user.email", "practice@example.invalid")
    git(target, "config", "commit.gpgsign", "false")
    value = {"part": number, "token": token, "workdir": str(target)}
    if number == 1:
        index = rng.randrange(5)
        memory = ["1", "2", "3", "4", "5"]
        memory[index] = str(rng.randrange(20, 90))
        (target / "src/partner/memory.txt").write_text("\n".join(memory) + "\n", encoding="utf-8")
        value["task"] = "Запусти boot.py, объясни сообщение и код возврата; исправь только данные и покажи код 0. Объясни одну выбранную пиром команду quest1.sh."
    elif number == 2:
        value["branch"] = "probe/" + token
        value["task"] = "Создай указанную ветку от develop. Создай src/probe.txt со своим объяснением merge, сделай коммит; добавь строку с токеном карточки, сделай второй коммит. Слей в develop отдельным merge-коммитом. Объясни родителей merge."
    elif number == 3:
        orders = [["product", "sum", "quotient", "difference"], ["quotient", "difference", "sum", "product"], ["difference", "product", "quotient", "sum"]]
        value.update(prefix="Канал-" + token + ": ", order=rng.choice(orders))
        value["task"] = "Перед Hello добавь указанный prefix, n/a оставь прежним. В calc измени порядок четырёх результатов на order: sum=сумма, difference=разность, product=произведение, quotient=частное. Проверка ввода и отсутствие переноса сохраняются. До запуска предскажи вывод, после объясни каждую правку."
    elif number == 4:
        value.update(cx=rng.choice([-3, -2, 1, 2, 3]), cy=rng.choice([-3, -1, 1, 3]),
                     radius=rng.choice([3, 4, 6, 7, 8]), inclusive=rng.choice([False, True]))
        value["task"] = "Передатчик перенесён в (cx, cy), радиус radius. inclusive=true: граница входит; false: не входит. Измени signal.py, предскажи ответы в центре, на границе и снаружи, объясни формулу и сравнение."
    elif number == 5:
        import re
        text = (target / "src/errors.md").read_text(encoding="utf-8")
        entries = re.findall(r"^##\s+\d+\..+$", text, flags=re.M)
        value["entry"] = rng.choice(entries) if entries else "Пир выбирает одну запись из журнала."
        value["task"] = "Пир самостоятельно поднимает ещё одну копию по HOWTO. Автор воспроизводит выбранную запись в practice5: для ошибки восстанавливает её условия, для успешной проверки запускает её и объясняет результат. Пир просит изменить одно входное значение; автор заранее объясняет ожидаемое изменение. Это намеренный эксперимент, не CRASH сдаваемой версии."
    else:
        phrase = "ПИР " + "".join(rng.choice("АБВГДЕЖЗИКЛМНОПРСТУФХЦЧШЭЮЯ ") for _ in range(rng.randrange(17, 70))) + " " + token
        folder = target / "probe data"
        folder.mkdir()
        source = folder / "source.txt"
        source.write_text(" ".join("%04x" % ord(x) for x in phrase) + "\n", encoding="utf-8")
        value.update(phrase=phrase, source="probe data/source.txt", output="probe data/restored")
        value["task"] = "Запусти quest6.sh с аргументами source и output из карточки. Объясни маски, аргументы и кавычки. Пир переименовывает выходную папку в аргументе; повтори прогон. Перечисления конкретных файлов и готового ответа в скрипте нет."
    write_json(path, value)
    print(json.dumps(value, ensure_ascii=False, indent=2))
    print("Карточка фиксируется один раз. Практика — в workdir; сданный commit не меняется.")


def probe(args):
    review = Path(args.review).resolve()
    source = review / ("card%d.json" % args.part)
    if not source.is_file():
        raise ValueError("Карточка %d ещё не выдана. Сначала выполни: "
                         "python3 tools/day1.py card %s --part %d"
                         % (args.part, args.review, args.part))
    c = json.loads(source.read_text(encoding="utf-8"))
    repo = Path(c["workdir"])
    rows = []
    if args.part == 1:
        result = command([sys.executable, "src/partner/boot.py"], repo)
        unchanged = all((repo / "src/partner" / n).read_bytes() == (ROOT / "src/partner" / n).read_bytes()
                        for n in ["boot.py", "memory_loader.py"])
        rows = [{"matches": result.returncode == 0 and unchanged, "exit": result.returncode,
                 "modules_unchanged": unchanged}]
    elif args.part == 2:
        base = git(review / "submitted", "rev-parse", "HEAD")
        new = git(repo, "rev-list", "--count", "--no-merges", base + ".." + c["branch"])
        merge = git(repo, "rev-list", "--min-parents=2", base + "..develop")
        tip = git(repo, "rev-parse", c["branch"])
        parents = git(repo, "show", "-s", "--format=%P", "develop").split()
        note = command(["git", "show", "develop:src/probe.txt"], repo)
        rows = [{"matches": int(new) >= 2 and bool(merge) and tip in parents and note.returncode == 0 and c["token"].encode() in note.stdout,
                 "commits": int(new), "merge": merge}]
    elif args.part == 3:
        for value in ["+19", "-8", "  42  ", "²", "1 2", ""]:
            valid = value.strip().lstrip("+-").isascii() and value.strip().lstrip("+-").isdigit()
            expected = c["prefix"] + "Hello, " + str(int(value)) + "!" if valid else "n/a"
            rows.append(run_case(repo, "hello.py", value + "\n", expected))
        for a, b in [(8, 2), (-7, 2), (99999999999999999999, 3), (1, 0)]:
            q = abs(a) // abs(b) * (-1 if (a < 0) != (b < 0) else 1) if b else "n/a"
            values = dict(sum=a+b, difference=a-b, product=a*b, quotient=q)
            rows.append(run_case(repo, "calc.py", "%s %s\n" % (a,b), " ".join(str(values[k]) for k in c["order"])))
        rows.append(run_case(repo, "calc.py", "три 2\n", "n/a"))
    elif args.part == 4:
        x, y, r = c["cx"], c["cy"], c["radius"]
        for a,b,expect in [(x,y,"IN"),(x+r,y,"IN" if c["inclusive"] else "OUT"),(x+r+1,y,"OUT"),(x-r,y,"IN" if c["inclusive"] else "OUT")]:
            rows.append(run_case(repo,"signal.py", "%s %s\n" % (a,b),expect))
        rows.append(run_case(repo,"signal.py","1,5 2\n","n/a"))
        # Обязательно включаем точку, отличающую новое правило от исходного.
        # Одни центр и три осевые точки иногда случайно совпадают у двух кругов.
        bound = abs(x) + abs(y) + r + 6
        found = False
        for a in range(-bound, bound + 1):
            for b in range(-bound, bound + 1):
                distance = (a - x) * (a - x) + (b - y) * (b - y)
                new_rule = distance <= r*r if c["inclusive"] else distance < r*r
                if new_rule != (a*a + b*b < 25):
                    rows.append(run_case(repo, "signal.py", "%s %s\n" % (a,b), "IN" if new_rule else "OUT"))
                    found = True
                    break
            if found:
                break
    elif args.part == 5:
        print("Журнал, HOWTO, объяснение и наблюдаемое самостоятельное действие проверяет пир. Автоматического зачёта нет.")
        return
    else:
        result = command(["bash", "src/quest6.sh", c["source"], c["output"]], repo)
        output = result.stdout.decode("utf-8", "replace")
        dest = repo / c["output"]
        remaining = list(dest.iterdir()) if dest.is_dir() else []
        rows = [{"matches": result.returncode == 0 and output.splitlines()[-1:] == [c["phrase"]]
                 and len(remaining) == len(c["phrase"]) and all(p.is_file() and p.name.startswith("part") and p.suffix == ".frag" for p in remaining),
                 "stdout": output, "exit": result.returncode}]
    write_json(review / ("probe%d.json" % args.part), rows)
    for row in rows:
        if not row["matches"]:
            if "input" in row:
                print("Расхождение: %s %r — ожидалось %r, получено %r"
                      % (row["script"], row["input"], row["expected"], row.get("stdout")))
            else:
                print("Расхождение: " + json.dumps(row, ensure_ascii=False)[:300])
    matched = sum(r["matches"] for r in rows)
    print("Наблюдаемые результаты: %d/%d. Объяснение и самостоятельность отмечает пир." % (matched, len(rows)))
    if matched < len(rows):
        print("Хотя бы одно расхождение означает, что карточка не выполнена: "
              "часть проверок совпадает и у неизменённого решения.")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="action", required=True)
    p = sub.add_parser("start"); p.add_argument("--name", required=True); p.add_argument("--email", required=True)
    p = sub.add_parser("pack"); p.add_argument("--out", required=True)
    p = sub.add_parser("intake"); p.add_argument("submission"); p.add_argument("--out", required=True)
    p = sub.add_parser("verify"); p.add_argument("review")
    for name in ["card", "probe"]:
        p = sub.add_parser(name); p.add_argument("review"); p.add_argument("--part",type=int,choices=range(1,7),required=True)
    args = parser.parse_args()
    try:
        globals()[args.action](args)
    except (ValueError, OSError, KeyError, subprocess.TimeoutExpired, json.JSONDecodeError) as error:
        print("Не удалось выполнить действие: " + str(error), file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
