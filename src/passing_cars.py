import itertools
from collections import deque
def solution(A):
    idxes = range(0, len(A))
    zeros = [idx for idx, item in enumerate(A) if item ==0]
    ones = set(idxes) - set(zeros)

    allcombis = itertools.product(zeros, ones)
    valid = itertools.filterfalse(lambda tpl: tpl[1] < tpl[0], allcombis)

    counter = itertools.count()
    deque(zip(valid, counter), maxlen=0)  # (consume at C speed)
    res =  next(counter)

    return -1 if res > 1000000000 else res

