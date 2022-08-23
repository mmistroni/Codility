import unittest
from src.tape_equlibrium import solution

class MyTestCase(unittest.TestCase):
    def test_something(self):
        A = [3, 1, 2, 4, 3]
        res = solution(A)
        self.assertEquals(1, solution(A))

if __name__ == '__main__':
    unittest.main()
