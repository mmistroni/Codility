import unittest
from src.genomic_range_query import  solution
class MyTestCase(unittest.TestCase):
    def test_something(self):
        S = 'CAGCCTA'
        P = [2,5,0]
        Q = [4,5,6]
        expected = [2,4,1]
        self.assertEqual(expected, solution(S,P,Q))  # add assertion here

if __name__ == '__main__':
    unittest.main()
