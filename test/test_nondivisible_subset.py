import unittest
from non_divisible_subset import solution

class MyTestCase(unittest.TestCase):
    def test_something(self):

        S = [1, 7, 2, 4]
        k = 3

        res = solution(S, k)
        self.assertEqual(3, res)


    def test_something2(self):
        S = [19, 10, 12,10, 24, 25,22]
        k = 4

        res = solution(S, k)
        self.assertEqual(3, res)

    def test_something3(self):
        S = [ 1, 2, 3, 4, 5, 6 ]
        k = 3

        res = solution(S, k)
        self.assertEqual(3, res)


if __name__ == '__main__':
    unittest.main()
