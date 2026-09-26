"""Загрузочный модуль напарника.

Выданный модуль. Править нельзя.

Запуск:
    python3 src/partner/boot.py

Пытается поднять загрузчик памяти и сообщает, чем дело кончилось.
Свой код возврата берёт у загрузчика: ноль — память поднялась, не ноль — нет.
"""

import os
import subprocess
import sys

LOADER = "memory_loader.py"


def here():
    return os.path.dirname(os.path.abspath(__file__))


def main():
    print("...")
    print("Привет. Я загрузочный модуль. Кажется, у нас проблемы.")
    print("Я не вижу остальных модулей. Если честно, мне немного одиноко.")
    print("Не говоря уж о том, что мне нечего запускать.")
    print("Кажется, что-то нашёл. Попробую поднять память...")
    print("-" * 46)

    loader = os.path.join(here(), LOADER)
    if not os.path.isfile(loader):
        print("ОШИБКА: загрузчик памяти не найден: " + loader)
        sys.exit(1)

    result = subprocess.run([sys.executable, loader])

    print("-" * 46)
    if result.returncode == 0:
        print("Так-то лучше. Память на месте, дальше я сам.")
        print("Закинь этот файл в репозиторий, чтобы он не потерялся.")
    else:
        print("Неудача. Память не поднялась, я снова один.")
        print("Посмотри, что сказал загрузчик, — там всё написано.")

    sys.exit(result.returncode)


main()
