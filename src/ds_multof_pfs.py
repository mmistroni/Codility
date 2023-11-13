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

def  printDivisors(n):
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

def is_good(tst):
    # there should be an intersection between prime divisors and factors
    F = arrayF(tst)
    factors = factorization(tst, F)
    res = printDivisors(tst)
    return sum(res) % sum(factors) == 0


def solution(nMin, nMax):
    res = []
    for i in range(nMin, nMax+1):
        if is_good(i):
            res.append(i)
    return res