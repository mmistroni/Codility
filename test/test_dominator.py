import unittest
from src.dominator import solution

class MyTestCase(unittest.TestCase):
    def test_something(self):
        A = [3,  4, 3, 2,  3, -1, 3 , 3]
        self.assertEquals(3, solution(A))


if __name__ == '__main__':
    unittest.main()
