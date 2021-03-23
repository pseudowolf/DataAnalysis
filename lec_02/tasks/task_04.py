from itertools import combinations, combinations_with_replacement


def get_combinations(s, k) -> tuple:
    return list(combinations(s, k))

def get_combinations_with_replacement(s, k):
    return list(combinations_with_replacement(s, k))


print(get_combinations('ABCDE', 2))
print(get_combinations_with_replacement('abcd', 2))

