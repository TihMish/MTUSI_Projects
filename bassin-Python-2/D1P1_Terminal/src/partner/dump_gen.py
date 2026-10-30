"""Разворачивает дамп памяти напарника в папку dump/.

Выданный модуль. Править нельзя.

Запуск:
    python3 dump_gen.py            # развернёт dump.txt
    python3 dump_gen.py файл       # развернёт указанный файл

Папка dump/ создаётся в той директории, из которой запущена команда.
Если папка уже есть, она разворачивается заново — испортить дамп
и начать сначала не страшно.

Отдельный режим для проверяющего:
    python3 dump_gen.py --new "ФРАЗА" > новый_дамп.txt

В этом режиме модуль ничего не разворачивает: он печатает дамп,
собранный из фразы. Так на проверке порождается дамп, которого
проверяемый не видел, — брать закрытый файл ни у кого не нужно.
Фраза набирается обычными буквами и знаками, до 999 символов.
"""

import os
import random
import shutil
import sys
import argparse
from pathlib import Path

DUMP_DIR = "dump"
JUNK_COUNT = 300
NOISE_COUNT = 25
NOISE_ALPHABET = "0123456789abcdefghijklmnopqrstuvwxyz"
CELLS_PER_LINE = 12
MAX_CELLS = 999


def read_source(path):
    """Читает дамп: коды ячеек по четыре шестнадцатеричные цифры."""
    if not os.path.isfile(path):
        print("Файл дампа не найден: " + path)
        sys.exit(1)

    with open(path, encoding="utf-8") as source:
        cells = source.read().split()

    if len(cells) == 0:
        print("Дамп пуст: " + path)
        sys.exit(1)

    if len(cells) > MAX_CELLS or any(len(cell) != 4 or any(c not in "0123456789abcdefABCDEF" for c in cell) for cell in cells):
        print("Некорректный дамп: нужны 1–999 ячеек по четыре hex-цифры.")
        sys.exit(1)
    if any(not chr(int(cell, 16)).isprintable() for cell in cells):
        print("Дамп содержит непечатаемый символ.")
        sys.exit(1)
    return cells


def make_dump(text):
    """Печатает дамп, собранный из фразы. Ничего не разворачивает."""
    codes = []
    for symbol in text:
        code = ord(symbol)
        if code > 0xFFFF or not symbol.isprintable():
            print("Символ не помещается в ячейку: " + symbol)
            print("Возьми фразу из обычных букв и знаков.")
            sys.exit(1)
        codes.append("%04x" % code)

    if len(codes) == 0:
        print("Пустая фраза. Укажи её так: dump_gen.py --new \"ФРАЗА\"")
        sys.exit(1)

    if len(codes) > MAX_CELLS:
        print("Фраза длиннее " + str(MAX_CELLS) + " символов.")
        sys.exit(1)

    for start in range(0, len(codes), CELLS_PER_LINE):
        print(" ".join(codes[start:start + CELLS_PER_LINE]))


def make_dir():
    target = Path(DUMP_DIR).resolve()
    cwd = Path.cwd().resolve()
    if target == cwd or cwd not in target.parents or Path(DUMP_DIR).is_symlink():
        print("Папка дампа должна быть отдельной подпапкой текущей папки.")
        sys.exit(1)
    relative = target.relative_to(cwd)
    if relative.parts[0] in {"src", "materials", "datasets", "tools", "templates", ".git"}:
        print("Нельзя разворачивать дамп в папку исходников или Git.")
        sys.exit(1)
    if target.exists():
        if not target.is_dir() or any(not p.is_file() or p.is_symlink() or not p.name.startswith(("part", "chunk", "noise")) for p in target.iterdir()):
            print("В папке есть посторонние объекты; выбери новую папку дампа.")
            sys.exit(1)
        shutil.rmtree(str(target))
    target.mkdir(parents=True)


def write_file(name, content):
    with open(os.path.join(DUMP_DIR, name), "w", encoding="utf-8") as target:
        target.write(content)


def unpack(cells):
    """Раскладывает ячейки дампа вперемешку с мусором."""
    random.seed(len(cells))

    for number, cell in enumerate(cells, 1):
        write_file("part%03d.frag" % number, cell + "\n")

    for number in range(1, JUNK_COUNT + 1):
        write_file("chunk%04d.dat" % number, "")

    for number in range(1, NOISE_COUNT + 1):
        garbage = "".join(random.choice(NOISE_ALPHABET) for _ in range(12))
        write_file("noise%02d.frag" % number, garbage + "\n")


def main():
    global DUMP_DIR
    parser = argparse.ArgumentParser(description="Развернуть дамп или создать его из фразы.")
    parser.add_argument("source", nargs="?", default=os.path.join(os.path.dirname(os.path.abspath(__file__)), "dump.txt"))
    parser.add_argument("--new", metavar="ФРАЗА")
    parser.add_argument("--dir", default="dump")
    args = parser.parse_args()
    if args.new is not None:
        make_dump(args.new)
        return
    DUMP_DIR = args.dir
    cells = read_source(args.source)
    make_dir()
    unpack(cells)

    total = len(cells) + JUNK_COUNT + NOISE_COUNT
    print("Дамп развёрнут в папку " + DUMP_DIR + "/")
    print("Восстановлено объектов: " + str(total))
    print("Целостность не проверялась.")


main()
