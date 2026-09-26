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

n5 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(n5[:3])
print(n5[-3:])
print(n5[2:7])
print(n5[::2])
print(n5[::-1])















