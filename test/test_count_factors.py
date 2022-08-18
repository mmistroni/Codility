import unittest
from src.count_factors import solution, divisors

class MyTestCase(unittest.TestCase):
    def test_something(self):

        self.assertEquals(8, solution(24))

    def test_something2(self):
        print(divisors(24))


if __name__ == '__main__':
    unittest.main()
