import unittest
from largest_string import solution

class MyTestCase(unittest.TestCase):
    def test_something(self):
        S = "ababb"
        self.assertEqual("baaaa", solution(S))

    def test_something2(self):
        S = "abbbabb"
        self.assertEqual("babaaaa", solution(S))

    def test_something3(self):
        S = "aaabab"
        self.assertEqual("aaabab", solution(S))


if __name__ == '__main__':
    unittest.main()
