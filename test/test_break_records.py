import unittest

from break_records import solution
class MyTestCase(unittest.TestCase):
    def test_something(self):
        test_input = [12,24,10,24]
        self.assertEqual((1,1), solution(test_input))

    def test_something2(self):
        test_input = [10, 5, 20, 20, 4, 5, 2, 25, 1]
        self.assertEqual((2,4), solution(test_input))

    def test_something3(self):
        test_input = [3, 4, 21, 36, 10, 28, 35, 5, 24, 42]
        self.assertEqual((4, 0), solution(test_input))


if __name__ == '__main__':
    unittest.main()
