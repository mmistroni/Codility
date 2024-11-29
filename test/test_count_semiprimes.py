import unittest

from src.count_semiprimes import solution, factorization, arrayF
from itertools import permutations, product
class MyTestCase(unittest.TestCase):


    def _find_factors(self, A):
        primes = []
        for item in range(1,20):
            F = arrayF(item)

            factors = set(factorization(item, F))
            if not factors:
                primes.append(item)
        return primes

    def test_find_factors(self):
        A = list(range(1, 26))
        primes = self._find_factors(A)
        primes.pop(0)
        p = [tpl[0] * tpl[1] for tpl in product(primes, repeat=2) if tpl[0] * tpl[1] <=26]

        print(set(p))

    def test_something(self):
        P = [ 1, 4 , 16]
        Q= [ 26, 10, 20]
        expected = [10, 4, 0]
        res = solution(26, P, Q)

        self.assertEqual(expected, res)


if __name__ == '__main__':
    unittest.main()
