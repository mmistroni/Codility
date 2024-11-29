import unittest

from src.brackets import solution
class MyTestCase(unittest.TestCase):
    def test_nested(self):
        nested = "{[()()]}"
        self.assertEqual(1, solution(nested))

    def test_not_nested(self):
        not_nested =  "([)()]"
        self.assertEqual(0, solution(not_nested))

    def test_not_nested(self):
        not_nested =  ")("
        self.assertEqual(0, solution(not_nested))


if __name__ == '__main__':
    unittest.main()
