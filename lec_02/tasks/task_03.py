"""
Написать функцию, принимающую строку s и число n
и возвращающую всевозможные перестановки из n символов в s строке
в лексикографическом(!) порядке (использовать itertools.permutations)
"""
from itertools import permutations


def permutations_in(string, n):
    """
    a function that takes a string s and a number n
    and returns all possible permutations of n characters in s string
    in lexicographic order
    :param string:
    :param n:
    :return list:
    """
    return list(permutations(string, n))

print(permutations_in('ABCD', 4))
