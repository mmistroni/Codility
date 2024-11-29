import unittest
from src.max_counters2 import solution

class MyTestCase(unittest.TestCase):
    def test_something(self):
        A = 24
        self.assertEqual(8, solution(A))


if __name__ == '__main__':
    unittest.main()
