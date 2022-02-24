import unittest

from src.triangular_triplets import solution
class MyTestCase(unittest.TestCase):
    def test_something(self):
        A = [ 10, 2, 5, 1, 8,20]
        self.assertEqual(1, solution(A))


if __name__ == '__main__':
    unittest.main()
