# -*- coding: utf-8 -*-
"""Пример разбора журнала. Выдан готовым, менять его не нужно.

    python3 src/partner/example.py

Считает, сколько раз помощник вызвал каждый инструмент.
Используй как образец: открыть файл, разобрать строку, накопить счётчик.
"""
import json
from pathlib import Path

КОРЕНЬ = Path(__file__).resolve().parents[2]

def мой_вариант():
    """Буква варианта из src/variant.txt. Её выдают на бумажной карточке помощника."""
    файл = КОРЕНЬ / "src/variant.txt"
    if not файл.exists():
        raise SystemExit(
            "Не найден файл src/variant.txt.\n"
            "Возьми бумажную карточку помощника, найди на ней букву варианта\n"
            "и создай файл src/variant.txt с одной этой буквой внутри.")
    буква = файл.read_text(encoding="utf-8").strip().upper()[:1]
    if not (КОРЕНЬ / "datasets" / буква).exists():
        raise SystemExit(f"Варианта {буква!r} нет. В src/variant.txt впиши букву с карточки: "
                         + ", ".join(sorted(п.name for п in (КОРЕНЬ / "datasets").iterdir()
                                            if п.is_dir())))
    return буква

ЖУРНАЛ = КОРЕНЬ / "datasets" / мой_вариант() / "logs/agent.jsonl"

счётчик = {}
with ЖУРНАЛ.open(encoding="utf-8") as файл:
    for строка in файл:
        запись = json.loads(строка)
        имя = запись["tool"]
        счётчик[имя] = счётчик.get(имя, 0) + 1

for имя in счётчик:
    print(имя, счётчик[имя])
