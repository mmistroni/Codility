# https://www.codewars.com/kata/56b0f5f84de0afafce00004e/train/python

import math


def is_coprime(a, b):
    return math.gcd(a, b) == 1

def relatively_prime (n, l):
    return [item  for item in l if is_coprime(n, item)]