import unittest
from src.distinct_elems import solution

class MyTestCase(unittest.TestCase):
    def test_something(self):

        A = [2 ,  1,  1, 2 ,  3  ,  1]

        self.assertEqual(3, solution(A))  # add assertion here


if __name__ == '__main__':
    unittest.main()
