# База Python из первых дней

## Значения и ввод

```python
line = input()
parts = line.split()
if len(parts) == 2:
    try:
        a = int(parts[0])
        b = int(parts[1])
    except ValueError:
        result = "n/a"
```

int принимает краевые пробелы и знак: int(" +19 ") возвращает 19.
float("1.5") работает, float("1,5") вызывает ValueError. Проверка isdigit()
не заменяет преобразование целого со знаком. Делитель проверяется до деления.

## Списки, словари, циклы

```python
values = [2, 4, 6]
total = 0
for value in values:
    total += value
average = total / len(values)
counts = {}
for name in ["A", "B", "A"]:
    if name not in counts:
        counts[name] = 0
    counts[name] += 1
```

Пустой набор требует отдельного решения: делить на len([]) нельзя.
append меняет список. Присваивание b=a для списка не создаёт независимую копию.
Индекс отсчитывается с нуля; -1 означает последний элемент непустого списка.

## Функции и форматирование

```python
def mean(total, count):
    if count == 0:
        return None
    return total / count

value = mean(12, 3)
print(format(value, ".2f"))
```

return возвращает результат вызвавшему коду; print отправляет текст в поток.
Функция без выполненного return возвращает None. Импорт подключает модуль;
в обычном процессе повторный import уже загруженного модуля не исполняет его
заново автоматически. Код при импорте тоже имеет побочные эффекты.

## Файлы и ошибки

```python
with open("data.txt", encoding="utf-8") as stream:
    for line in stream:
        fields = line.rstrip("\n").split("|")
```

with здесь — справка для реализации проекта, не дополнительная тема вопросов
по дням 1–2. Можно использовать pathlib.read_text. Перехватывайте ожидаемую
ошибку возле операции, которая может её вызвать. Не подменяйте ошибочные данные
выдуманными нулями, если договор этого не разрешает.
