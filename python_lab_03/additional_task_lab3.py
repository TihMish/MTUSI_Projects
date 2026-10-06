def average(data):
    total = 0
    for x in data:
        total += x
    return total / len(data)


def min_max(data):
    mn = data[0]
    mx = data[0]
    for x in data:
        if x < mn:
            mn = x
        if x > mx:
            mx = x
    return mn, mx


def count_above(data, limit=100):
    count = 0
    for x in data:
        if x > limit:
            count += 1
    return count


def find_index(data, value):
    for i in range(len(data)):
        if data[i] == value:
            return i
    return -1


def closest_to_average(data, avg):
    ordered = sorted(data, key=lambda x: abs(x - avg))
    return ordered[:3]


def analyze(data, value):
    avg = average(data)
    mn, mx = min_max(data)
    print("Данные:", data)
    print("Среднее:", avg)
    print("Минимум:", mn)
    print("Максимум:", mx)
    print("Выше 100 мс:", count_above(data))
    print("Индекс значения", value, ":", find_index(data, value))
    print("Три ближайших к среднему:", closest_to_average(data, avg))
    print()


analyze([42, 38, 51, 35, 57, 120, 44, 39], 57)
analyze([40, 41, 250, 39, 42], 250)
analyze([42, 38, 51, 35, 57, 120, 44, 39], 999)
