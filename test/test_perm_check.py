import unittest
from Codility.src.perm_check import solution

class MyTestCase(unittest.TestCase):
    def test_something(self):
        A = [4,1,3,2]
        self.assertEquals(1, solution(A))  # add assertion here

    def test_something2(self):
        A = [4, 1, 3]

        self.assertEqual(0, solution(A))  # add assertion here


if __name__ == '__main__':
    unittest.main()
