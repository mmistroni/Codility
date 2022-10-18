import unittest

from problem3 import solution

class MyTestCase(unittest.TestCase):
    def test_something(self):
        A = [2,1,3]
        S = 2
        self.assertEqual(3, solution(A,S))  # add assertion here

    def test_something2(self):
        A = [0, 4, 3, -1]
        S = 2
        self.assertEqual(2, solution(A, S))  # add assertion here

    def test_something2(self):
        A = [2, 1, 4]
        S = 3
        self.assertEqual(0, solution(A, S))  # add assertion here

if __name__ == '__main__':
    unittest.main()
