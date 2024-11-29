import unittest
from src.minimum_loss import solution

class MyTestCase(unittest.TestCase):
    def test_something(self):
        prices = [20, 15, 8, 2, 12]

        res = solution(prices)
        self.assertEqual(3, res)

    def test_something2(self):
        prices = [5, 10, 3]
        res = solution(prices)
        self.assertEqual(2, res)

    def test_something3(self):
        prices = [20, 7, 8, 2, 5]
        res = solution(prices)
        self.assertEquals(2, res)


if __name__ == '__main__':
    unittest.main()
