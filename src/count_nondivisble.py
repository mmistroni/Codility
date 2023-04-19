#https://app.codility.com/programmers/lessons/11-sieve_of_eratosthenes/count_non_divisible/
from collections import OrderedDict

def find_bigger(item, arr):
    return [i for i in arr if i> item]

def find_smallest(item, arr):
    smallest =  [i for i in arr if i < item and item % i !=0]
    F = arrayF(item)
    factors = set(factorization(item, F))

    return len([f for f in factors if f in smallest])


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


def solution(arr):

    holder_dict = {}
    res = []
    for item in arr:
        if item not in holder_dict.keys():
            bigger = find_bigger(item, arr)
            smaller = find_smallest(item, arr)
            total = len(bigger) + smaller
            holder_dict[item] = total
        res.append(holder_dict[item])
    return res