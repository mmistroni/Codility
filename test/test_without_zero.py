import unittest
from src.without_two_zeros import zeros

class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(zeros(1), 2)

    def test_two(self):
        self.assertEqual(zeros(2), 2)

    def test_three(self):
        self.assertEqual(zeros(3), 3)
    

if __name__ == '__main__':
    unittest.main()
