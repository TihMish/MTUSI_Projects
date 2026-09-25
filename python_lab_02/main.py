# Задание 3

# print("Hello, World!")


# Задание 4

# n4, a4, h4, s4 = "Настя", 18, 165, True

# print(n4, a4, h4, s4, sep='\n')
# print(type(n4), type(a4), type(h4), type(s4), sep='\n')

# a4, h4 = 19, 168
# print(a4, h4, sep='\n')



# Задание 5

# print("Задание 5. Введите по очереди: имя, фамилию, возраст, рост")
# n5, f5, a5 = input("Имя: "), input("Фамилия: "), input("Возраст: ")
# print(n5, f5, a5, sep='\n')

# a5 = int(a5)
# h5 = float(input("Рост: "))

# print(a5, type(a5), h5, type(h5), sep='\n')



# Задание 6

# a6, b6 = 15, 4
# print(a6 + b6, a6 - b6, a6 * b6, a6 / b6, a6 // b6, a6 % b6, a6 ** b6, sep='\n')
# print(2 + 3 * 4, (2 + 3) * 4, sep='\n')



# Задание 7

# a7, b7 = float(input("Число 1: ")), float(input("Число 2: "))
# print(a7 + b7, a7 - b7, a7 * b7, a7 / b7, sep='\n')


# Задание 8

# for i8 in range(1, 11):
#     print(i8)

# for i8 in range(10, 0, -1):
#     print(i8)

# for i8 in range(0, 21, 2):
#     print(i8)

# for i8 in range(0, 21, 4):
#     print(i8)


# Задание 9

# n9, s9 = int(input("n: ")), 0
# for i9 in range(1, n9 + 1):
#     s9 += i9
# print(s9)


# Задание 10

# c10 = 10
# while c10 >= 1:
#     print(c10)
#     c10 -= 1
# print("Цикл завершён")


# Задание 11

# import math
# r11 = 12
# print(2 * math.pi * r11, math.pi * r11 ** 2, math.sqrt(225), sep='\n')


# Задание 12

n12 = int(input("Число: "))
if n12 > 0:
    print("Число положительное")
elif n12 < 0:
    print("Число отрицательное")
else:
    print("Число равно нулю")
print("Число чётное" if n12 % 2 == 0 else "Число нечётное")






