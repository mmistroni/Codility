#https://www.codewars.com/kata/60d2325592157c0019ee78ed

def gauss(n):
    return (n * (n + 1)) /2


def S(n):
    return gauss(n)

def Z(n):
    return sum([S(i) for i in range(1, n + 1)])


def sum_of_sums(n):
    zetas = Z(n)
    return S(zetas)