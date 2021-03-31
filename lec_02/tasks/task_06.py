"""
Генератор, выводящий первые fn чисел Фибоначчи.
"""
def get_fibonacci(n):
    i = 1
    f1 = f2 = 1
    for _ in range(i, n+1):
        if i in (1, 2):
            yield f1
        else:
            f1, f2 = f2, f1 + f2
            yield f2
        i += 1

F = get_fibonacci(10)

print(*F)