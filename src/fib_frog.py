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

    return [f for f in fib if f <= limit] if limit else fib

def new_algo(A):

    ''' TODO  Need to handle this special case which we didnt consider

        The goal is to count the minimum number of jumps in which the frog can get to the other side of the river
         (from position −1 to position N).
        The frog can jump between positions −1 and N (the banks of the river) and every position containing a leaf.


    '''


    # The frog can jump over any distance F(K), where F(K) is the K-th Fibonacci number.
    # Not quite right.
    # 1. we need to exclude the zeros as it's not a jump
    # 2. We need to look at combinations from 2 to max ones
    # 3. We start with  two jumps.if not we do combi of 3
    # 1. Find good fibonacci seq which covers potential jumps in the array

    one_jump = len(A) + 1


    fib_seq = [f for f in  fibonacci_seq(len(A) + 1, len(A)) if f > 0]

    if one_jump in fib_seq:
        return 1


    # Find how many ones
    ones = [idx for idx in range(0, len(A)) if A[idx] == 1] + [len(A) + 1]

    if not ones:
        return -1


    diffs = [(idx+1) for idx in ones]

    combilen = len(ones)

    # 2, all possible combinations of fibonacci which sums
    # to len(A) + 1

    good_tpls = []


    for clen in range(2, combilen+1):
        for p in product(fib_seq, repeat=clen):
            if sum(p) == len(A) + 1:
                if p[0] in diffs:
                    #good_tpls.append(p)
                    return  len(p)
    return -1




def solution(A):
    return new_algo(A)