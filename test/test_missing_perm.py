import unittest
from Codility.src.missing_perm import sol

class MyTestCase(unittest.TestCase):
    def test_something(self):
        A = [2, 3, 1 ,5]
        self.assertEqual(4, sol(A))


if __name__ == '__main__':
    unittest.main()
