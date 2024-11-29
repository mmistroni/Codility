import unittest

from src.picking_numbers import solution


class MyTestCase(unittest.TestCase):
    def test_something(self):
        t = [1,1,2,2,4,4,5,5,5]

        self.assertEqual(5, solution(t))


    def test_something2(self):
        t = [4, 6, 5, 3, 3, 1]
        self.assertEqual(3, solution(t))


    def test_something3(self):
        t = [1, 2, 2, 3, 1, 2]
        self.assertEqual(5, solution(t))

if __name__ == '__main__':
    unittest.main()
