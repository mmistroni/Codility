import unittest

from src.distinct import solution
class MyTestCase(unittest.TestCase):
    def test_something(self):
        A = [2, 1, 1, 2, 3, 1]

        self.assertEqual(3, solution(A))


if __name__ == '__main__':
    unittest.main()
