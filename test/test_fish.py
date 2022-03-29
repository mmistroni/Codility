import unittest

from src.fish import solution
class MyTestCase(unittest.TestCase):
    def test_something(self):
        A = [4,3,2,1,5]
        B = [0,1,0,0,0]

        res = solution(A,B)

        self.assertEqual(2,res , res )


if __name__ == '__main__':
    unittest.main()
