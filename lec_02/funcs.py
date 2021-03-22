def f(x):
    print(f'calculating {x}*10')
    return x * 10

A = (1, 2, 3, 4, 5, 6)
B = (f(x) for x in A)
for y in B:
    print(y)

def double_perform(f, x):
    return f(f(x))

def f1(x):
    return x * 10
def f2(x):
    return x * x
def f3(x):
    return -x
for f in f1, f2, f3:
    print(double_perform(f, 5))

a = range(10)
b = (x for x in a if x % 2 == 0)
print(*b)
print(*map(lambda x: x*x, a))

a = (1, 2, 3, 4, 5)
b = tuple(x*10 for x in a)
c = zip(a, b)
i = iter(c)
for a, b in c:
    print(a, b)

for num, char in enumerate('HELLO'):
    print(num, char)

print(*map(lambda a: a[0]*a[1], enumerate('HELLO')))

def arithm_progression(start, stop, step):
    x = start
    while x < stop:
        print(f'now working on x = {x}')
        yield x
        x += step

A = arithm_progression(1, 10, 2)

for x in A:
    print(x)



y = map(int, input("Enter a multiple value: ").split())
print(y)
x = list(y)
print("List of students: ", x)