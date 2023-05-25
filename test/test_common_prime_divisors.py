import unittest

from common_prime_divisors import solution


def gcd(a, b, res):
    if a == b:
        return res * a
    elif (a % 2 == 0) and (b % 2 == 0):
        return gcd(a // 2, b // 2, 2 * res)
    elif (a % 2 == 0):
        return gcd(a // 2, b, res)
    elif (b % 2 == 0):
        return gcd(a, b // 2, res)
    elif a > b:
        return gcd(a - b, b, res)
    else:
        return gcd(a, b - a, res)

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


class MyTestCase(unittest.TestCase):


    # Not good, It finds also the composite factors
    def find_factors(self, tst):

        F = arrayF(tst)
        factors = set(factorization(tst, F))

        return factors

    def test2(self):
        N = [15, 10, 9]
        M = [75, 30, 5]

        for one, two in zip(N, M):


            factors = self.find_factors(one)




            factors2 = self.find_factors(two)
            print(f'Factors of {one}:{factors}|{two}:{factors2}')

    def test1(self):
        N = [15, 10, 9]
        M = [75, 30, 5]
        res = solution(N, M)
        self.assertEqual(1, res)

if __name__ == '__main__':
    unittest.main()
