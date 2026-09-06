"""Загрузчик памяти напарника.

Выданный модуль. Править нельзя.

Читает memory.txt, лежащий рядом с этим файлом. Память исправна, если в файле
ровно пять подмодулей, по одному в строке, и номер каждого совпадает с его
местом в списке. При любом отклонении загрузка прерывается и процесс
завершается с ненулевым кодом.
"""

import os
import sys

EXPECTED = 5


def memory_path():
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), "memory.txt")


def read_lines(path):
    if not os.path.isfile(path):
        print("ОШИБКА: файл памяти не найден: " + path)
        sys.exit(1)

    with open(path, encoding="utf-8", errors="replace") as source:
        return [line.strip() for line in source if line.strip() != ""]


def main():
    lines = read_lines(memory_path())

    if len(lines) > EXPECTED:
        print("ОШИБКА: обнаружены данные после пятого подмодуля.")
        sys.exit(1)

    for index, line in enumerate(lines, 1):
        if line != str(index):
            print("ОШИБКА: при загрузке подмодуля " + str(index) +
                  " ожидался номер " + str(index) + ", найдено: " + line)
            sys.exit(1)
        print("ЗАГРУЗКА ПОДМОДУЛЯ " + line + " ПРОШЛА УСПЕШНО")

    if len(lines) < EXPECTED:
        print("ОШИБКА: не хватает подмодулей. Загружено " + str(len(lines)) +
              " из " + str(EXPECTED) + ".")
        sys.exit(1)

    print("ПАМЯТЬ ЗАГРУЖЕНА: " + str(EXPECTED) + " подмодулей.")
    sys.exit(0)


main()
