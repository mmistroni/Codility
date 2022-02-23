import unittest
from Codility.src.mushroom_picker import solution

class MyTestCase(unittest.TestCase):
    def test_something(self):
        A =[2, 3, 5, 1, 3, 9]

        k = 4
        m = 6
        self.assertEqual(25, solution(A,k, m)) # add assertion here


if __name__ == '__main__':
    unittest.main()
