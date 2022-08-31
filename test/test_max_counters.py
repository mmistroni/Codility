import unittest

from src.max_counters import solution

class MyTestCase(unittest.TestCase):
    def test_something(self):
        A = [3,  4, 4, 6, 1, 4, 4]
        N = 5

        res = solution(N, A)
        expected = [3, 2, 2, 4, 2]
        self.assertEqual(expected, res)

    def test_something2(self):
        A = [3]
        N = 5

        res = solution(N, A)
        expected = [3, 2, 2, 4, 2]
        self.assertEqual(expected, res)


if __name__ == '__main__':
    unittest.main()
