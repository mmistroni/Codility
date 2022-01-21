import unittest

from Codility.src.odd_occurrences import solution
class MyTestCase(unittest.TestCase):
    def test_something(self):
        A = [9,3,9,3,9,7,9]

        self.assertEqual(7, solution(A))  # add assertion here


if __name__ == '__main__':
    unittest.main()
