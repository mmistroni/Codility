from src.matrix_trace import trace

import unittest

from src.max_profit import solution

class MyMatrixTestCase(unittest.TestCase):
    
    def test1(self):
        self.assertEqual(trace([[1,2,3], [4,5,6], [7,8,9]]), 15)
    
    def test2(self):
        self.assertEqual(trace([[0,0], [0,0]]), 0)

    def test3(self):
        self.assertEqual(trace([[1]]), 1)

    def test4(self):
        self.assertEqual(trace([]), None)

    def test5(self):
        self.assertEqual(trace([[1,2,3], [4,5,6]]), None)

if __name__ == '__main__':
    unittest.main()
