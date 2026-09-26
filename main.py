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







