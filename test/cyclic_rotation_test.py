import unittest

from src.cyclic_rotation import  sol

class MyTestCase(unittest.TestCase):
    def test_something(self):
        A = [3, 8, 9, 7, 6]
        K = 3
        res = sol(A, K)
        self.assertEqual([9, 7, 6, 3, 8], res)  # add assertion here


    def test_something2(self):
        A = [0,0,0]
        K = 1
        res = sol(A, K)
        self.assertEqual([0,0,0], res)  # add assertion here

    def test_something3(self):
        A = [1, 2, 3, 4]
        K = 4
        res = sol(A, K)
        self.assertEqual([1, 2, 3, 4], res)  # add assertion here


if __name__ == '__main__':
    unittest.main()
