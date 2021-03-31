a = (1, 2, 3, 4, 5)
b = (10, 20, 30, 40, 50, 60)
c = ('a', 'b', 'c', 'd')
abc = zip(a, b, c)

print('zip result: ', *abc)

def my_zip(*iterables):
    result = ()
    i = 0
    l = []
    for object in iterables:
        try:
            _ = iter(object)
        except TypeError:
            print(object, 'is not iterable')

        l.append(len(object))


    while i < min(l):
        r = []
        for obj in iterables:
            r.append(obj[i])

        i += 1
        yield tuple(r)



abc = my_zip(a, b, c)

print('my_zip result: ', *abc)

