def build():
    return [1, 2]
a = build()
b = build()
a.append(3)
print(len(a), len(b))
