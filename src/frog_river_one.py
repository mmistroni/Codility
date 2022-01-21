from itertools import dropwhile


def _loop(X, A, checks, idx):
    if not A:
        return -1
    item = A[0]
    if item in checks:
        checks.remove(item)
    if not checks:
        return idx
    return _loop(X, A[1:], checks, idx+1)



def solution(X, A):
    # WRONG we need to detect when we have leafts in
    # every position in range(0,n-1)up to N
    # we need to keep a set of element from 1 to n
    # and while we scan we need to keep track of the index
    avail = list(range(1, X+ 1))
    return _loop(X, A, avail, 0)
