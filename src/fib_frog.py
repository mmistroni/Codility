#https://app.codility.com/programmers/lessons/13-fibonacci_numbers/fib_frog/

def fibonacci(n):
    fib = [0] * (n+2)
    fib[1] = 1
    for i in range(2, n+1):
        fib[i] = fib[i-1] + fib[i-2]
    return fib[n]


def solution(A):
    return 0