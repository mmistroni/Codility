import unittest

from src.toptal3 import install_filters

class MyTestCase(unittest.TestCase):
    def test_something1(self):
        A = [5, 19, 8, 1]

        self.assertEqual(3, install_filters(A))

    def test_something2(self):
        A = [10, 10]

        self.assertEqual(2, install_filters(A))

    def test_something3(self):
        A = [3, 0, 5]
        self.assertEqual(2, install_filters(A))

if __name__ == '__main__':
    unittest.main()
