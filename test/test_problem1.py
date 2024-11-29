import unittest

from src.problem1 import solution

class MyTestCase(unittest.TestCase):
    def test_something(self):
        T = [''] * 5
        T[0] = "test1a"
        T[1] = "test2"
        T[2] = "test1b"
        T[3] = "test1c"
        T[4] = "test3"
        R = [''] * 5
        R[0] = "Wrong answer"
        R[1] = "OK"
        R[2] = "Runtime error"
        R[3] = "OK"
        R[4] = "Time limit exceeded"

        self.assertEqual(33, solution(T,R))  # add assertion here

    def test_something2(self):
        T = [''] * 5
        T[0] = "codility1"
        T[1] = "codility3"
        T[2] = "codility2"
        T[3] = "codility4b"
        T[4] = "codility4a"
        R = [''] * 5
        R[0] = "Wrong answer"
        R[1] = "OK"
        R[2] = "OK"
        R[3] = "Runtime error"
        R[4] = "OK"

        self.assertEqual(50, solution(T, R))  # add assertion here

if __name__ == '__main__':
    unittest.main()
