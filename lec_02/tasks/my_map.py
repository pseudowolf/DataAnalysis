

def my_map(f, iterable):
    for element in iterable:
        yield f(element)

a = [1, 2, 3, 4, 5]

def f1(e):
    return e*e

print(*map(f1, a))
print(*my_map(f1, a))
