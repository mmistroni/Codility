import unittest
from nesting import solution

class MyTestCase(unittest.TestCase):
    def test_nested(self):
        self.assertEqual(1, solution("(()(())())"))

    def test_not_nested(self):
        self.assertEqual(0, solution("())"))

if __name__ == '__main__':
    unittest.main()
