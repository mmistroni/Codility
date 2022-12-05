import unittest
from carol_of_code import solution

class MyTestCase(unittest.TestCase):
    def test_something(self):
        A =  ["RGBW", "GBRW"],
        self.assertEqual(1, solution(A))

    def test_something2(self):
        A = ["WBGR", "WBGR", "WRGB", "WRGB", "RBGW"]
        self.assertEqual(4, solution(A))

    def test_something3(self):
        A =  ["RBGW", "GBRW", "RWGB", "GBRW"],
        self.assertEqual(2, solution(A))

    def test_something4(self):
        A = ["GBRW", "RBGW", "BWGR", "BRGW"]
        self.assertEqual(2, solution(A))


if __name__ == '__main__':
    unittest.main()
