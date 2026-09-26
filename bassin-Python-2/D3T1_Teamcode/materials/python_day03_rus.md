# Python для дней 03–04

Все примеры доступны офлайн. Реализация использует стандартную библиотеку.

## Словарь и связи

```python
by_id = {}
by_id[101] = {"id": 101, "level": 3}
answers_by_id = {}
answers_by_id.setdefault(101, []).append({"label": "А", "correct": True})
```

ID не обязан совпадать с индексом списка. Не теряйте дубликаты при чтении:
сначала посчитайте частоты ID, затем исключите все записи с повторённым ID.

## Множества и сортировка

```python
used = set()
used.add(101)
available = [q for q in questions if q["id"] not in used]
available = sorted(available, key=lambda q: q["id"])
```

Множество не хранит пригодный для воспроизводимости порядок. Для случайного
выбора сначала упорядочьте список. Словарь в современных Python сохраняет
порядок вставки, но разные источники вставки всё равно дают разные порядки.

## Случайность

```python
import random
rng = random.Random(seed)
question = rng.choice(available)
```

Не выбирайте из пустого списка. Один объект rng на сессию. Один seed работает
при одинаковом порядке данных и последовательности обращений к генератору.

## Файлы и исключения

```python
from pathlib import Path
path = Path(folder) / "bank_reference.txt"
text = path.read_text(encoding="utf-8")
for line in text.splitlines():
    if not line.strip() or line.lstrip().startswith("#"):
        continue
    fields = [part.strip() for part in line.split("|")]
```

Проверяйте число полей до распаковки. Обрабатывайте ожидаемую ошибку записи
около этой записи. Ошибка открытия основной папки — ошибка запуска, а отсутствие
фрагмента одного вопроса — битость этого вопроса. Не ловите всё вокруг программы.

## CLI

Можно использовать sys.argv или argparse — argparse входит в стандартную библиотеку.
Проверяйте обязательный путь, значение после --seed, конфликт флагов и неизвестные флаги.
`sys.exit(2)` — ненулевой код при неверном запуске.

## Диалог и JSON в логе

```python
import json
import sys
print("> " + question_text)
print("ОТВЕТ:", flush=True)
try:
    answer = input()
except EOFError:
    answer = None
encoded = json.dumps(answer, ensure_ascii=False)
print(log_line, file=sys.stderr, flush=True)
```

input снимает завершающий перевод строки, но не пробелы. None нельзя перепутать
с пустой строкой: это EOF. JSON сохраняет различие между null и "" и экранирует
кавычки/управляющие символы. Поле ответа в log_line берётся из encoded.

## Модули

main.py импортирует bank и engine. Файлы рядом в src; __init__.py не требуется.
Модули возвращают данные, печатает main.py. Избегайте круговых зависимостей:
банк не должен зависеть от состояния движка. Не всякий круговой import сразу
падает, но такой договор хрупок и усложняет понимание.

Самостоятельный пример разбора аргументов и диалога — cli_example_rus.md.
