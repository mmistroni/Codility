# https://app.codility.com/programmers/lessons/11-sieve_of_eratosthenes/count_semiprimes/
'''
A prime is a positive integer X that has exactly two distinct divisors: 1 and X. The first few prime integers are 2, 3, 5, 7, 11 and 13.

A semiprime is a natural number that is the product of two (not necessarily distinct) prime numbers. The first few semiprimes are 4, 6, 9, 10, 14, 15, 21, 22, 25, 26.

You are given two non-empty arrays P and Q, each consisting of M integers. These arrays represent queries about the number of semiprimes within specified range
Query K requires you to find the number of semiprimes within the range (P[K], Q[K]), where 1 ≤ P[K] ≤ Q[K] ≤ N.

Alternatively check https://en.wikipedia.org/wiki/Semiprime
or use ifilters
'''
from itertools import combinations_with_replacement

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


# Next attempt
def factorization(x, F):
    # we just need to check for items in array which are smaller than
    # our factor.
    # for items that are smaller or equal than our number
    # then we find multiples and remove from array
    # what is left is what is non-divisible

    primeFactors = []
    while (F[x] > 0):
        primeFactors += [F[x]]
        x //= F[x]
        primeFactors += [x]
    return primeFactors

def _find_primes(A):
    primes = []
    for item in A:
        F = arrayF(item)

        factors = set(factorization(item, F))
        if not factors:
            primes.append(item)
    return primes

def solution(N, P, Q):
    tmp = []
    holder = []
    for start, end in zip(P, Q):
        primlist = list(range(2, end + 1))

        primes = _find_primes(primlist)

        combis = combinations_with_replacement(primes, 2)

        good = [i for i in combis if start <= i[0] * i[1] <= end]

        uniques = len(set(good))
        tmp.append(uniques)



    return tmp