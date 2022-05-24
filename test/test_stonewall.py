
import unittest

from src.stonewall import  solution
class MyTestCase(unittest.TestCase):
    def test_something(self):
        A = [8, 8,  5, 7, 9,  8, 7, 4,  8]
        self.assertEqual(7, solution(A))

    def test_wrong(self):
        A = [1,1,1]
        self.assertEqual(1, solution(A))

    def test_wrong2(self):
        A = [1, 2, 3, 3, 2, 1]
        self.assertEquals(3, solution(A))




if __name__ == '__main__':
    unittest.main()
