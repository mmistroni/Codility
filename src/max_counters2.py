import itertools
from collections import deque

def solution(A):

    valids = (i for i in range(1, A+1) if A % i == 0)
    counter = itertools.count()
    deque(zip(valids, counter), maxlen=0)  # (consume at C speed)
    return next(counter)