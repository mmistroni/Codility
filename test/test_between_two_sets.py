import unittest

from between_two_sets import solution

class MyTestCase(unittest.TestCase):
    def test_something(self):
        a = [2,6]
        b = [24,36]
        self.assertEqual(2, solution(a, b))

    def test_something2(self):
        a = [2,6]
        b = [24,36]
        self.assertEqual(2, solution(a, b))



if __name__ == '__main__':
    unittest.main()
