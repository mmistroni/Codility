import itertools
from collections import deque

def count_iter_items(iterable):
    """
    Consume an iterable not reading it into memory; return the number of items.
    """
    counter = itertools.count()
    deque(zip(iterable, counter), maxlen=0)  # (consume at C speed)
    return next(counter)

def solution(A):
    return count_iter_items (k for k in dict.fromkeys(A).keys())
