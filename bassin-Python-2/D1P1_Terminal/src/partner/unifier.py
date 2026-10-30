"""Сборщик сообщения из развёрнутого дампа.

Выданный модуль. Править нельзя.

Запуск:
    python3 unifier.py

Читает папку dump/ в текущей директории. Если собрать сообщение удалось,
записывает его в message.txt и печатает на экран. Если нет — печатает
«Ошибка.» и завершается с кодом 1.
"""

import os
import sys
import argparse

DUMP_DIR = "dump"
RESULT_FILE = "message.txt"
HEX_DIGITS = "0123456789abcdefABCDEF"


def fail():
    print("Ошибка.")
    sys.exit(1)


def fragment_number(name):
    """Возвращает номер фрагмента или None, если имя не подходит."""
    if not name.startswith("part") or not name.endswith(".frag"):
        return None

    digits = name[len("part"):-len(".frag")]
    if len(digits) != 3 or not digits.isdigit():
        return None

    return int(digits)


def read_cell(path):
    """Возвращает код ячейки или None, если содержимое не годится."""
    if not os.path.isfile(path):
        return None

    with open(path, encoding="utf-8", errors="replace") as source:
        tokens = source.read().split()

    if len(tokens) != 1 or len(tokens[0]) != 4:
        return None

    for symbol in tokens[0]:
        if symbol not in HEX_DIGITS:
            return None

    return int(tokens[0], 16)


def collect():
    if not os.path.isdir(DUMP_DIR):
        fail()

    names = os.listdir(DUMP_DIR)
    if len(names) == 0:
        fail()

    cells = {}
    for name in names:
        number = fragment_number(name)
        if number is None:
            fail()

        code = read_cell(os.path.join(DUMP_DIR, name))
        if code is None:
            fail()

        cells[number] = code

    for number in range(1, len(cells) + 1):
        if number not in cells:
            fail()

    return "".join(chr(cells[number]) for number in range(1, len(cells) + 1))


def main():
    global DUMP_DIR
    parser = argparse.ArgumentParser(description="Собрать сообщение из папки фрагментов.")
    parser.add_argument("--dir", default="dump")
    args = parser.parse_args()
    DUMP_DIR = args.dir
    message = collect()

    with open(RESULT_FILE, "w", encoding="utf-8") as target:
        target.write(message + "\n")

    print("Сообщение собрано.")
    print(message)


main()
