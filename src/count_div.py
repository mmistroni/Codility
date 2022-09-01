'''
Write a function:

def solution(A, B, K)

that, given three integers A, B and K, returns the number of integers within the range [A..B] that are divisible by K, i.e.:

{ i : A ≤ i ≤ B, i mod K = 0 }

For example, for A = 6, B = 11 and K = 2, your function should return 3, because there are three numbers divisible by 2 within the range [6..11], namely 6, 8 and 10.

Write an efficient algorithm for the following assumptions:

A and B are integers within the range [0..2,000,000,000];
K is an integer within the range [1..2,000,000,000];
A ≤ B.


'''
import itertools
from collections import deque
def solution(A, B, K):

    startiterator = itertools.dropwhile(lambda i: i % K != 0, range(A, B+1))

    try:
        start = next(startiterator)
    except Exception as e:
        return 0

    divs = range(start, B+1, K)
    counter = itertools.count()
    deque(zip(divs, counter), maxlen=0)  # (consume at C speed)
    return next(counter)
