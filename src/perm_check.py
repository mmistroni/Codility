from itertools import permutations, filterfalse
def solution(A):

    maxN = max(A)

    if len(A) != maxN:
        return 0
    else:

        for i in range(1, maxN+1):
            try:
                A.remove(i)
            except Exception as e:
                return 0
        return 1
