# Задание 1

# def greet(name):
#     print("Здравствуйте,", name)
 
# def square(number):
#     return number ** 2
 
# def max_of_two(a, b):
#     return a if a > b else b
 
# greet("Настя")
# greet("Кирилл")
 
# print(square(4), square(-7))
# print(max_of_two(10, 3), max_of_two(-5, -1))


# Задание 2

# def calculate_rectangle(width, height):
#     return width * height

# def calculate_perimeter(width, height):
#     return 2 * (width + height)

# def describe_rectangle(width, height, unit="см"):
#     print(f"Прямоугольник {width}{unit} x {height}{unit}")

# print(calculate_rectangle(5, 3), calculate_rectangle(10, 2))
# print(calculate_perimeter(5, 3), calculate_perimeter(10, 2))

# describe_rectangle(5, 3)
# describe_rectangle(4, 2, "м")


# Задание 3

# value = 10

# def example():
#     value = 20
#     l3 = "локальная переменная задания 3"
#     print(value, l3)

# example()
# print(value)

# try:
#     print(l3)
# except NameError as e:
#     print("Ошибка:", e)


# Задание 4

# n4 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

# print(n4[0], n4[2], n4[-1])

# n4[1] = 200
# n4.append(110)
# n4.remove(30)

# print(n4, len(n4))


# Задание 5

# n5 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# print(n5[:3])
# print(n5[-3:])
# print(n5[2:7])
# print(n5[::2])
# print(n5[::-1])


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










