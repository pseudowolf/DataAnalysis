
a = ['0', '1', '2', '3', '4', '5']

aa = enumerate(a)

print(*aa)

def my_enum(iterable):
    i = 0
    for obj in iterable:
        yield (i, obj)
        i += 1

aa = my_enum(a)

print(*aa)