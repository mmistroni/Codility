import unittest

from src.max_profit import solution

class MyTestCase(unittest.TestCase):
    def test_something(self):
        A = [23171, 21011, 21123, 21366, 21013, 21367]
        self.assertEqual(356, solution(A))

if __name__ == '__main__':
    unittest.main()
