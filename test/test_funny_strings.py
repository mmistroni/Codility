import unittest
from funny_strings import solution

class MyTestCase(unittest.TestCase):

    def test_something(self):
        s = 'lmnop'
        self.assertEqual("Funny", solution(s))

    def test_something2(self):
        s = 'acxz'
        self.assertEqual("Funny", solution(s))

    def test_something3(self):
        s = 'bcxz'
        self.assertEqual("Not Funny", solution(s))



if __name__ == '__main__':
    unittest.main()
