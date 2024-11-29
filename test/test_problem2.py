import unittest
from src.problem2 import solution

class MyTestCase(unittest.TestCase):
    def test_something(self):
        A = [None] * 8
        A[0] = 7
        A[1] = 3
        A[2] = 7
        A[3] = 3
        A[4] = 1
        A[5] = 3
        A[6] = 4
        A[7] = 1
        self.assertEqual(7, solution(A))  # add assertion here

    def test_something(self):
        A = [2,1,1,3,2,1,1,3]
        self.assertEqual(3, solution(A))  # add assertion here


if __name__ == '__main__':
    unittest.main()
