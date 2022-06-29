from src.max_slice_sum import solution
import unittest

class MyTestCase(unittest.TestCase):
    def test_something(self):
        A = [3,2,-6,4,0]
        self.assertEquals(5, solution(A))

    def test_something2(self):
        A = [-10]
        self.assertEquals(-10, solution(A))


if __name__ == '__main__':
    unittest.main()
