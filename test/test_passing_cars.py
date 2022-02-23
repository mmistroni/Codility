import unittest
from passing_cars import solution

class MyTestCase(unittest.TestCase):
    def test_something(self):
        A = [0, 1, 0, 1, 1]
        self.assertEquals(5, solution(A))


if __name__ == '__main__':
    unittest.main()
