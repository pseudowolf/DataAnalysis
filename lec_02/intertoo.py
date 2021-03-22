from itertools import *
from functools import *




for p in permutations('ABCD'):
    print(*p)

A = tuple(range(1, 6))
print(reduce(lambda x , y: x+y, A))


