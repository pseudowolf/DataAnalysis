from itertools import combinations


def get_combinations(s, k) -> tuple:
    return tuple(combinations(s, k))


print(get_combinations('ABCDE', 4))
