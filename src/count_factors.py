import math
from collections import deque
from itertools import count

def divisors(n):
    i = 1
    result = 0
    while (i * i < n):
        if (n % i == 0):
            result += 2
        i += 1
    if (i * i == n):
        result += 1
    return result

def solution(n):
    return divisors(n)
    iterable = (i for i in range(1, n + 1) if n % i == 0)
    counter = count()
    deque(zip(iterable, counter), maxlen=0)  # (consume at C speed)
    return next(counter)
