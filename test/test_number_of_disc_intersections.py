import unittest

from number_of_disc_intersections import Solution


class MyTestCase(unittest.TestCase):
    def test_something(self):
        A = [1, 5, 2, 1, 4, 0]

        res = Solution(A)

        self.assertEqual(11, res)  # add assertion here


if __name__ == '__main__':
    unittest.main()
