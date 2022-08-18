import math
from collections import deque
from itertools import count

def solution(n):
    iterable = (i for i in range(1, n + 1) if n % i == 0)
    counter = count()
    deque(zip(iterable, counter), maxlen=0)  # (consume at C speed)
    return next(counter)
