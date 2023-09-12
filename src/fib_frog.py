#https://app.codility.com/programmers/lessons/13-fibonacci_numbers/fib_frog/
from collections import defaultdict
import heapq
from itertools import takewhile
from itertools import product, combinations_with_replacement

def fibonacci_seq(n, limit=None):
    fib = [0] * (n+2)
    fib[1] = 1
    for i in range(2, n+1):
        fib[i] = fib[i-1] + fib[i-2]
        if limit and fib[i] == limit:
            return fib

    return [f for f in fib if f <= limit] if limit else fib

def new_algo(A):

    one_jump = len(A) + 1
    fib_seq = [f for f in  fibonacci_seq(len(A) + 2, len(A)+2) if f > 0]

    if one_jump in fib_seq:
        # direct jump to the end
        return 1

    # Looking for leafs

    # Find how many ones
    ones = [idx for idx in range(0, len(A)) if A[idx] == 1]

    if not ones:
        return -1

    # adding start and end
    ones = [-1] + ones +  [len(A)]

    diffs = [(idx+1) for idx in ones] # difference between first element and all subsequent 1s

    combilen = len(ones)

    # Looping for all possible combination of fibonacci numbers which sums up to len[A] + 1
    for clen in range(2, combilen+1):
        for p in product(fib_seq, repeat=clen):
            if sum(p) == len(A) + 1:
                curidx = -1
                for item in p:
                    nxt = item + curidx
                    if nxt not in ones:
                        curidx = -1
                        break
                    else:
                        curidx = nxt
                if curidx == -1:
                    continue
                else:
                    return len(p)

    return -1

    # Last session https://app.codility.com/demo/results/trainingQD59DY-JY5/


def solution(A):
    return new_algo(A)