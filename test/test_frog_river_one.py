import unittest

from src.frog_river_one import solution

class MyTestCase(unittest.TestCase):
    def test_something(self):
        A = [1,3,1,4,2,3,5,4]
        res = solution(5,A)
        self.assertEquals(6 , res)

    def test_something2(self):
        A = [2,2,2,2,2,2]
        res = solution(3,A)
        self.assertEquals(-1 , res)


if __name__ == '__main__':
    unittest.main()
