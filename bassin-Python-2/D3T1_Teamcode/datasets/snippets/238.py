def f(x):
    return int(x)
try:
    r = f("a")
except ValueError:
    r = "n/a"
print(r)
