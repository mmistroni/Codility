#https://www.codewars.com/kata/60d2325592157c0019ee78ed

def gauss(n) -> int:
    return (n * (n + 1)) / 2


def S(n) -> int:
    return gauss(n)

def Z(n) -> int:

    '''
    holder = 0
    for i in range(1, n + 1):
        holder += S(i)

    return holder
    '''
    result = [0]
    # Gauss sum for 0 is 0
    res = 0
    for i in range(1, n + 1):
        result.append(result[-1] + i)
    return sum(result)

def sum_of_sums(n):
    zetas = Z(n)
    return S(zetas)