# Маленький пример CLI и состояния

Пример ниже — самостоятельная программа, не готовый тест. Сохраните во временном
файле вне src, запустите `python3 demo_cli.py текст --seed 7` и затем `--scan`.
argparse, json и random входят в стандартную библиотеку.

```python
import argparse
import json
import random
import sys

parser = argparse.ArgumentParser()
parser.add_argument("folder")
parser.add_argument("--scan", action="store_true")
parser.add_argument("--seed", type=int)
args = parser.parse_args()
if args.scan and args.seed is not None:
    parser.error("--scan несовместим с --seed")
if args.scan:
    print("Путь:", args.folder)
else:
    rng = random.Random(args.seed)
    print("> Демонстрационное число:", rng.choice([1, 2, 3]))
    print("ОТВЕТ:", flush=True)
    try:
        answer = input()
    except EOFError:
        answer = None
    print(json.dumps(answer, ensure_ascii=False), file=sys.stderr, flush=True)
```

Здесь папка только печатается как аргумент. В проекте её нужно открыть и проверить.
Отсутствующий обязательный аргумент, неверное число или неизвестный флаг argparse
обрабатывает подсказкой и ненулевым кодом; дополнительные конфликты задаёте сами.

Состояние знаний — обычный словарь с JSON-совместимыми значениями: числа,
строки, логические значения, None, списки и вложенные словари со строковыми ключами.
Не храните в нём файлы, генератор random или множество set. Это упрощает сравнение
состояния до и после операции. Для множества гипотез можно использовать список.

У engine.observe первый шаг — проверить, даёт ли ответ свидетельство. Если
результат «не принят» или scale=0, функция возвращает None без изменения словаря.
Номер хода, использованные ID и генератор случайности хранятся отдельно. Алгоритм
изменения знаний по верному/неверному ответу выбирает сама группа.
