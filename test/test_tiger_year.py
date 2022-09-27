import unittest
from tiger_year import solution

class MyTestCase(unittest.TestCase):
    def test_something(self):
        t = ["aab", "cab", "baa", "baa"]
        self.assertEqual(3, solution(t))

    def test_something2(self):
        T = ["zzz", "zbz", "zbz", "dgf"],
        self.assertEqual(2, solution(T))

    def test_something3(self):
        T = ["abc", "cba", "cab", "bac", "bca"]


if __name__ == '__main__':
    unittest.main()
