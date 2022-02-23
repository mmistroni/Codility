import unittest

from Codility.src.smallest_integer import solution

class MyTestCase(unittest.TestCase):
    def test_something(self):
        A = [1, 3, 6, 4, 1, 2]

        res = solution(A)
        self.assertEqual(5, res)  # add assertion here

    def test_something2(self):
        A = [-1, -3]

        res = solution(A)
        self.assertEqual(1, res)  # add assertion here


if __name__ == '__main__':
    unittest.main()
