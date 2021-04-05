"""
Генератор, выводящий первые n чисел Фибоначчи.
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

def gen_fibonacci(n):
    """Generates a Fibonacci series up to n."""
    a, b = 0, 1
    while a < n:
        yield a
        a, b = b, a + b

#F = get_fibonacci(10)

#print(*F)

print(*gen_fibonacci(100))