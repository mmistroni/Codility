import unittest

from common_prime_divisors import solution
from count_nondivisble import arrayF, factorization


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


class MyTestCase(unittest.TestCase):


    # Not good, It finds also the composite factors
    def find_factors(self, n):
        F = arrayF(n)
        factors = set(factorization(n, F))

        return factors

    def test2(self):
        N = [15, 10, 9]
        M = [75, 30, 5]

        for one, two in zip(N, M):
            factors = self.find_factors(one)
            factors2 = self.find_factors(two)
            print(f'Factors of {one}:{factors}|{two}:{factors2}')

    def test1(self):
        N = [15, 10, 30]
        M = [75, 30, 5]

        res = solution(N, M)
        self.assertEquals(1, res)


if __name__ == '__main__':
    unittest.main()
