import unittest
from bon_appetit import solution

class MyTestCase(unittest.TestCase):
    def test_something(self):
        bill = [3, 10, 2, 9]
        no_eat = 1
        charge = 12
        self.assertEqual(5, solution(bill, no_eat, charge))


if __name__ == '__main__':
    unittest.main()
