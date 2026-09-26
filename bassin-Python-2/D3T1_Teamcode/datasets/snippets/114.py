d = {}
for x in ["a", "b", "a"]:
    d[x] = d.get(x, 0) + 1
print(d["a"], d["b"])
