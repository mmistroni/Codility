import unittest

from src.kangaroo import solution

class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual("YES", solution(0,3,4,2))

    def test_something2(self):
        self.assertEqual("NO", solution(0, 2, 5, 3))



if __name__ == '__main__':
    unittest.main()
