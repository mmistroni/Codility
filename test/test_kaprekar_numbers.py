import unittest

from src.kaprekar_numbers import solution, is_kaprekar2
class MyTestCase(unittest.TestCase):
    def test_something(self):
        p, q = 1,100

        expected = [1, 9, 45, 55, 99]

        res = solution(p, q)

        self.assertEqual(expected, res)


    def test_kaprekar(self):


        expected = [1, 9, 45, 55, 99, 297, 703, 999, 2223,
                    2728, 4950, 5050, 7272, 7777, 9999,
                    17344, 22222, 77778, 82656, 95121, 99999]
        res = solution(1, 99999)

        print(f'diff1 = {set(res) - set(expected)}')
        print(f'diff2 = {set(expected) - set(res)}')
        self.assertEqual(expected, res)


if __name__ == '__main__':
    unittest.main()
