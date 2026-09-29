# Задание 1
def greet(name):
    print("Здравствуйте,", name)

def square(number):
    return number ** 2

def max_of_two(a, b):
    return a if a > b else b

greet("Настя")
greet("Кирилл")

print(square(4), square(-7))
print(max_of_two(10, 3), max_of_two(-5, -1))


# Задание 2
def calculate_rectangle(width, height):
    return width * height

def calculate_perimeter(width, height):
    return 2 * (width + height)

def describe_rectangle(width, height, unit="см"):
    print(f"Прямоугольник {width}{unit} x {height}{unit}")

print(calculate_rectangle(5, 3), calculate_rectangle(10, 2))
print(calculate_perimeter(5, 3), calculate_perimeter(10, 2))

describe_rectangle(5, 3)
describe_rectangle(4, 2, "м")


# Задание 3
value = 10

def example():
    value = 20
    l3 = "локальная переменная задания 3"
    print(value, l3)

example()
print(value)

try:
    print(l3)
except NameError as e:
    print("Ошибка:", e)


# Задание 4
n4 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

print(n4[0], n4[2], n4[-1])

n4[1] = 200
n4.append(110)
n4.remove(30)

print(n4, len(n4))


# Задание 5
n5 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(n5[:3])
print(n5[-3:])
print(n5[2:7])
print(n5[::2])
print(n5[::-1])


# Задание 6
m6 = (12.5, 13.0, 11.8, 14.2, 12.9, 13.5, 12.1, 13.8)

print(m6[0], m6[-1], m6[2:5])

try:
    m6[0] = 99
except TypeError as e:
    print("Ошибка:", e)

f6, s6 = m6[0], m6[1]
print(f6, s6)

l6 = list(m6)
l6[0] = 99
m6 = tuple(l6)
print(m6)


# Задание 7
n7 = [12.5, 13.0, 11.8, 14.2, 12.9, 13.5, 12.1, 13.8]

print(len(n7), sum(n7), min(n7), max(n7), sum(n7) / len(n7))

s7 = sorted(n7)
print(s7, n7)

n7.sort()
print(n7)


# Задание 8
def calculate_sum(numbers):
    total = 0
    for n in numbers:
        total += n
    return total

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

n8 = [12.5, 13.0, 11.8, 14.2, 12.9, 13.5, 12.1, 13.8]

print(calculate_sum(n8), sum(n8))
print(find_min(n8), min(n8))
print(find_max(n8), max(n8))


# Задание 9
def find_element(numbers, target):
    for i in range(len(numbers)):
        if numbers[i] == target:
            return i
    return -1

n9 = [12.5, 13.0, 11.8, 14.2, 12.9]

print(find_element(n9, 11.8), find_element(n9, 100))


# Задание 10
def analyze(numbers):
    return min(numbers), max(numbers), sum(numbers) / len(numbers)

n10 = [12.5, 13.0, 11.8, 14.2, 12.9]
mn10, mx10, avg10 = analyze(n10)
print(mn10, mx10, avg10)


# Задание 11
n11 = [-10, 3, -2, 8, -5]

sn11 = sorted(n11)
sa11 = sorted(n11, key=lambda x: abs(x))

print(sn11, sa11)


# Задание 12
def calculate_average(measurements):
    total = 0
    for m in measurements:
        total += m
    return total / len(measurements)

def find_minimum(measurements):
    mn = measurements[0]
    for m in measurements:
        if m < mn:
            mn = m
    return mn

def find_maximum(measurements):
    mx = measurements[0]
    for m in measurements:
        if m > mx:
            mx = m
    return mx

def count_above_average(measurements):
    avg = calculate_average(measurements)
    count = 0
    for m in measurements:
        if m > avg:
            count += 1
    return count

def find_value(measurements, target):
    for i in range(len(measurements)):
        if measurements[i] == target:
            return i
    return -1

def analyze_measurements(measurements):
    return find_minimum(measurements), find_maximum(measurements), calculate_average(measurements)

m12 = [23, 45, 12, 67, 34, 89, 21, 56, 78, 40]
mn12, mx12, avg12 = analyze_measurements(m12)

print(len(m12), mn12, mx12, avg12, count_above_average(m12), find_value(m12, 67))
