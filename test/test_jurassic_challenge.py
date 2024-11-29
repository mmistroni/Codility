import unittest

from src.jurassic_challenge import solution

class MyTestCase(unittest.TestCase):

    def test_case1(self):
        X = [4, 0, 2, -2]
        Y = [4, 1, 2, -3]
        colors = "RGRR"
        res = solution(X, Y, colors )
        self.assertEquals(2, res)

    def test_case2(self):
        X = [1,  1, -1, -1]
        Y = [1, -1, 1, -1]
        colors = "RGRG"
        self.assertEqual(4, solution(X, Y, colors))  # add assertion here

    def test_case3(self):
        X = [1, 0, 0]
        Y = [0, 1, -1]
        colors = "GGR"
        self.assertEqual(0, solution(X, Y, colors))  # add assertion here

    def test_case4(self):
        X = [5, -5, 5]
        Y = [1, -1, -3]
        colors = "GRG"
        self.assertEqual(2, solution(X, Y, colors))  # add assertion here

    def test_case5(self):
        X = [3000, -3000, 4100, -4100, -3000]
        Y = [5000, -5000, 4100, -4100, 5000]
        colors = "RRGRG"
        self.assertEqual(2, solution(X, Y, colors))  # add assertion here




if __name__ == '__main__':
    unittest.main()
