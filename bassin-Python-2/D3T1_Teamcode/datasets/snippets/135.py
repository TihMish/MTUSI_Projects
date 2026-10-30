items = ["4", "x", "6"]
s = 0
for item in items:
    try:
        s += int(item)
    except ValueError:
        s += 0
print(s)
