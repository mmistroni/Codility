from itertools import combinations,dropwhile

def check(tpl):
    p, q, r = tpl

    return (p + q) > r and \
    (q + r) > p and \
    (r + p) > q

def solution(A):
    A.sort()

    combis = combinations(A, 3)

    res = dropwhile(lambda tpl: not check(tpl), combis)
    try :
        next(res)
        return 1
    except Exception as e:
        return 0

