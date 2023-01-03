import unittest
from birthday_bar import solution

class MyTestCase(unittest.TestCase):

    def test_something(self):
        s = [2, 2, 1, 3, 1]
        d = 4
        m = 2

        res =solution(s, d, m)

        self.assertEqual(2, res)


if __name__ == '__main__':
    unittest.main()
