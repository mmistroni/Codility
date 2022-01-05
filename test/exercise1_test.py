import unittest
from Codility.src.exercise1 import solve

class MyTestCase(unittest.TestCase):

    def test_something(self):
        tester = [1, 2, 3, 3, 3, 2, 5, 3, 1, 7]

        res = solve(tester)
        print(res)
        self.assertIsNotNone(res)  # add assertion here


if __name__ == '__main__':
    unittest.main()
