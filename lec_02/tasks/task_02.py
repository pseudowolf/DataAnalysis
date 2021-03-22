"""
Написать функцию, принимающую 2 списка и возвращающую декартово произведение (использовать itertools.product)
"""

from itertools import product


def cartesian_product(list1, list2):
    return product(list1, list2)


print(*cartesian_product(list(range(5)), ['a', 'b', 'c', 'd', 'e']))
