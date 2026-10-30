def calculate_average(numbers):
    return sum(numbers) / len(numbers)


def find_min(numbers):
    m = numbers[0]
    for n in numbers:
        if n < m:
            m = n
    return m


def find_max(numbers):
    m = numbers[0]
    for n in numbers:
        if n > m:
            m = n
    return m
