#https://www.codewars.com/kata/562c04fc8546d8147b000039/train/python

import unittest
from math import sqrt
from itertools import product, combinations


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

def  printDivisors2(tst, factors):
    tmp = set()
    for f in factors:
        tmp.add(f)

    for tpl in combinations(factors, 2):
        tmp.add(tpl[0] * tpl[1])
    tmp.add(1)
    tmp.add(tst)
    return tmp

def  printDivisors(n, factors=None):
    d = []
    for i in range(1, int(sqrt(n)) + 1):
        if (n % i == 0) :

            # If divisors are equal, print only one
            if (n / i == i):
                d.append(i)
                print( i);


            else : #// Otherwise print both
                d.append(i)
                d.append(n / i)
                print(f'{i}, { n / i}')

    return [int(n) for n in d]


def generateDivisors(curIndex, curDivisor, arr, holder):
    # Base case i.e. we do not have more
    # primeFactors to include
    # https://www.geeksforgeeks.org/generating-all-divisors-of-a-number-using-its-prime-factorization/
    if (curIndex == len(arr)):
        print(curDivisor, end=' ')
        holder.append(curDivisor)
        return

    for i in range(arr[curIndex][0] + 1):
        generateDivisors(curIndex + 1, curDivisor, arr, holder)
        curDivisor *= arr[curIndex][1]


def is_good(tst):
    # there should be an intersection between prime divisors and factors
    # Not good, it's timing out
    from collections import Counter
    F = arrayF(tst)
    factors = factorization(tst, F)

    curIndex = 0
    curDivisor = 1

    d = Counter(factors)
    arr = []
    for k, v in d.items():
        arr.append((v, k))

    # Generate all the divisors
    holder = []
    generateDivisors(curIndex, curDivisor, arr, holder)

    print(f'Holder:{holder}')

    res = holder
    return sum(res) % sum(factors) == 0


def solution(nMin, nMax):
    res = []
    for i in range(nMin, nMax+1):
        if is_good(i):
            res.append(i)
    return res

def ds_multof_pfs(nMin, nMax):
    return solution(nMin, nMax)