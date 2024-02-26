# https://www.mathsisfun.com/combinatorics/combinations-permutations.html
# https://www.codewars.com/kata/65cdd06eac0d2ad8ee6c6067


def factorial(n, acc=1):
    if n == 1:
        return acc
    else:
        return factorial(n-1, acc * n)


def solution(n, k):
    # Not good we need to write just one line

    # factorial = lambda n, k: n * factorial(n - 1) if n > 1 else 1

    if k == n:
        return 1
    elif k > n:
        return 0
    else:
        return factorial(n) / (factorial(k) * factorial(n-k))