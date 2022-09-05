import unittest

from src.count_div import solution
from src.prefix_sums import generate_prefix_sum, prefix_sums

class MyTestCase(unittest.TestCase):
    def test_something(self):
        A = 6
        B = 11
        K = 2
        self.assertEqual(3, solution(A, B, K))

    def test_wrong(self):
        A = [0, 0, 11]
        self.assertEqual(1, solution(*A))

    def test_wrong2(self):
        A = 11
        B = 345
        K = 17
        self.assertEqual(20, solution(A, B, K))


if __name__ == '__main__':
    unittest.main()
