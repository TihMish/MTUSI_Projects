print("Сколько будет чисел (n)?")
n = int(input())
total = 0
for i in range(n):
    total += float(input())
sr = total / n
print(sr)
if sr >= 80:
    print("Высокий результат")
elif sr >= 50:
    print("Средний результат")
else:
    print("Низкий результат")
