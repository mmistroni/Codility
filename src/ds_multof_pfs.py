#https://www.codewars.com/kata/562c04fc8546d8147b000039/train/python

import unittest
from math import sqrt
from itertools import product, combinations


from functools import reduce

def factors(n):
    return set(reduce(list.__add__,
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))



def arrayF(n):
    F = [0] * (n + 1)
    i = 2
    while (i * i <= n):
        if (F[i] == 0):
            k = i * i
            while (k <= n):
                if (F[k] == 0):
                    F[k] = i;
                k += i

        i += 1
    return F

def factorization(x, F):
    primeFactors = []
    while (F[x] > 0) :
        primeFactors += [F[x]]
        x //= F[x]
    primeFactors += [x]
    return primeFactors


def prime_factors(n):
    """Returns all the prime factors of a positive integer"""
    factors = []
    divisor = 2
    while n > 1:
        while n % divisor == 0:
            factors.append(divisor)
            n /= divisor
        divisor = divisor + 1
        if divisor*divisor > n:
            if n > 1:
                factors.append(n)
            break
    return factors



def generateDivisors(curIndex, curDivisor, arr, holder):
    # Base case i.e. we do not have more
    # primeFactors to include
    # https://www.geeksforgeeks.org/generating-all-divisors-of-a-number-using-its-prime-factorization/
    if (curIndex == len(arr)):
        holder.append(curDivisor)
        return

    for i in range(arr[curIndex][0] + 1):
        generateDivisors(curIndex + 1, curDivisor, arr, holder)
        curDivisor *= arr[curIndex][1]

def is_good(tst):
    # there should be an intersection between prime divisors and factors
    # Not good, it's timing out
    from collections import Counter
    # Need to improve the factorization
    #F = arrayF(tst)
    p_factors = prime_factors(tst) #factorization(tst, F)

    curIndex = 0
    curDivisor = 1

    d = Counter(p_factors)
    arr = []
    for k, v in d.items():
        arr.append((v, k))

    # Generate all the divisors
    holder = []
    generateDivisors(curIndex, curDivisor, arr, holder)

    res = factors(tst) #holder
    return sum(res) % sum(p_factors) == 0

def solution(nMin, nMax):
    res = []
    for i in range(nMin, nMax+1):
        if is_good(i):
            res.append(i)
    return res

def ds_multof_pfs(nMin, nMax):
    return solution(nMin, nMax)