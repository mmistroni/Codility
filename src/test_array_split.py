import unittest

from Codility.src.array_split import sol
class MyTestCase(unittest.TestCase):
    def test_something(self):
        A = [3,1,2,4,3]
        self.assertEqual(1, sol(A))

if __name__ == '__main__':
    unittest.main()
