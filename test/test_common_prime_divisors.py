import unittest

from common_prime_divisors import solution


class MyTestCase(unittest.TestCase):

    def test1(self):
        N = [15, 10, 30]
        M = [75, 30, 5]

        res = solution(N, M)
        self.assertEquals(1, res)


if __name__ == '__main__':
    unittest.main()
