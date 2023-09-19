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
        # No leafs, and no direct jump
        return -1

    # adding start and end
    ones = [-1] + ones +  [len(A)]

    combilen = len(ones) # this will determine  max length of the combinations

    # Looping for all possible combination of fibonacci numbers which sums up to len[A] + 1
    for clen in range(2, combilen+1):
        for p in product(fib_seq, repeat=clen):
            if sum(p) == len(A) + 1:
                curidx = -1 # starting from start and incrementing it for every item in the tuple
                            # this simulates jumping from leaf to leaf

                # we need to find a way to avoid the loop
                for item in p:
                    nxt = item + curidx # jumping from one leaf to the other
                    if nxt not in ones:
                        # if we dont land on a leaf, we break
                        curidx = -1
                        break
                    else:
                        curidx = nxt
                # out of the loop, curidx is either the index of the last leaf or
                # is -1
                if curidx == -1:
                    # check then tuple
                    continue
                else:
                    return len(p)
    # https://app.codility.com/c/run/training68EV7K-5XJ/
    return -1

def solution(A):
    return new_algo(A)