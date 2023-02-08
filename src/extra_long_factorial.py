#https://www.hackerrank.com/challenges/extra-long-factorials/problem?isFullScreen=true


def factorial(n , acc):
    if n ==1:
        return acc
    return factorial(n-1, n*acc)

def solution(n):
    return factorial(n, 1)