import unittest

from chocolates_by_numbers import solution

class MyTestCase(unittest.TestCase):
    def test_something(self):
        N, M = 10, 4
        expected = len([0, 4, 8, 2, 6])
        res = solution(N, M)
        self.assertEqual(expected, res)


    def test_large2(self):
        N = (3 ** 9) * (2 ** 14)
        M = (2 ** 14) * (2 ** 14)
        res = solution(N, M)

if __name__ == '__main__':
    unittest.main()
