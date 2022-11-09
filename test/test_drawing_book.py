import unittest
from drawing_book import solution


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(1, solution(5, 3))

    def test_something2(self):
        self.assertEqual(0, solution(5,4))


    def test_something3(self):
        self.assertEqual(1, solution(7, 4))

    def test_something3(self):
        self.assertEqual(3810, solution(37455, 29835))



if __name__ == '__main__':
    unittest.main()
