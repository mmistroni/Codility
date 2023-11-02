#https://www.codewars.com/kata/5b997b066c77d521880001bd/train/python
from itertools import permutations

def print_perms(start):
    idx = 0
    for i in permutations(start, len(start)):
        rest = [i - j for i, j in zip(start, i)]
        if 0 not in rest:
            idx += 1
    return idx

def fibonacci_seq(n, limit=None):
    fib = [0] * (n + 2)
    fib[1] = 1
    for i in range(2, n + 1):
        fib[i] =  (i) * (fib[i - 1] + fib[i - 2])
    return fib



def solution(array_length):
    res = fibonacci_seq(array_length)
    return res[array_length-1]
