import unittest

from kaprekar_numbers import solution
class MyTestCase(unittest.TestCase):
    def test_something(self):
        p, q = 1,100

        expected = [1, 9, 45, 55, 99]

        res = solution(p, q)

        self.assertEqual(expected, res)


if __name__ == '__main__':
    unittest.main()
