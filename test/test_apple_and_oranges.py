import unittest
from apple_and_orange import is_in_house, solution

class MyTestCase(unittest.TestCase):
    def test_something(self):
        s = 7
        t = 10
        a = 4
        b = 12

        apples = [2, 3, -4]
        oranges = [3, -2, -4]

        solution(s, t, a, b, apples, oranges)


if __name__ == '__main__':
    unittest.main()
