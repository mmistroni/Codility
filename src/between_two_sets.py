# https://www.hackerrank.com/challenges/between-two-sets/problem?isFullScreen=true&h_r=next-challenge&h_v=zen
'''
There will be two arrays of integers.
Determine all integers that satisfy the following two conditions:

1 - The elements of the first array are all factors of the integer being considered
2 - The integer being considered is a factor of all elements of the second array

'''
import math

def find_factors(num):
    from math import sqrt
    N = num
    temp1 = sqrt(N)
    temp2 = int(temp1)
    factors = [1, N]
    if (temp1 == temp2):
        for i in range(2, temp2):
            if (N % i == 0):
                factors.append(i)
                factors.append(N // i)
        factors.append(temp2)
    else:
        for i in range(2, temp2 + 1):
            if (N % i == 0):
                factors.append(i)
                factors.append(N // i)
    return factors


def find_all_factors_in_b(b):
    first_factors  = find_factors(b[0])
    for item in b[1:]:
        for f in first_factors:
            if item % f != 0:
                first_factors.remove(f)
    return [f for f in first_factors if f > 1]


def solution(a, b):

    factors_to_consider = find_all_factors_in_b(b)

    for f in factors_to_consider:
        check = [i % f ==0 for i in a]
        if not all(check):
            factors_to_consider.remove(f)
    return len(factors_to_consider)

