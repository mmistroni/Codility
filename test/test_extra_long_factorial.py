import unittest
from extra_long_factorial import solution

class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(120,  solution(5))

    def test_something2(self):
        self.assertEqual(15511210043330985984000000,  solution(25))

if __name__ == '__main__':
    unittest.main()
