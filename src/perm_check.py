from itertools import permutations
def solution(A):
    tpls = tuple(A)
    if max(A) != len(A):
        return 0
    for x in permutations(A):
        if x == tpls:
            return 1
    return 0