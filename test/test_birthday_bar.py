import unittest
from birthday_bar import solution

class MyTestCase(unittest.TestCase):

    def test_something(self):
        s = [2, 2, 1, 3, 2]
        d = 4
        m = 2

        res =solution(s, d, m)

        self.assertEqual(2, res)

    def test_something2(self):
        s = [1, 1, 1, 1, 1, 1]
        d = 3
        m = 2

        res =solution(s, d, m)

        self.assertEqual(0, res)

    def test_something3(self):
        s = [4]
        d = 4
        m = 1

        res =solution(s, d, m)

        self.assertEqual(1, res)


if __name__ == '__main__':
    unittest.main()
