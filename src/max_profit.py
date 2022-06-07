from itertools import combinations
def solution(A):
    tpl = [two - one for one, two in combinations(A, 2) if two > one]
    return max(tpl)

