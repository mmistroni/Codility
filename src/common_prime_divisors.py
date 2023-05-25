#https://app.codility.com/programmers/lessons/12-euclidean_algorithm/common_prime_divisors/


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

def factorization(x, F):
    primeFactors = []
    while (F[x] > 0) :
        primeFactors += [F[x]]
        x //= F[x]
    primeFactors += [x]
    return primeFactors

def find_factors(tst):

    F = arrayF(tst)
    factors = set(factorization(tst, F))

    return factors




# Hint : https://www.britannica.com/science/number-theory/Euclid
def solution(N, M):
    holder =0
    for one, two in zip(N, M):
        factors = find_factors(one)
        factors2 = find_factors(two)

        if factors == factors2:
            holder += 1

    return holder