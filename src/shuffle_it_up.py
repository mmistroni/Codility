#https://www.codewars.com/kata/5b997b066c77d521880001bd/train/python
from itertools import permutations

# refactor to use fib frog algo
def fibonacci_seq(n, limit=None):
    fib = [0] * (n + 2)
    fib[1] = 1
    for i in range(2, n + 1):
        fib[i] =  (i) * (fib[i - 1] + fib[i - 2])
    return fib

def solution(array_length):
    res = fibonacci_seq(array_length)
    return res[array_length-1]
