from src.beautiful_text import beautiful_text
import unittest

class MyTestCase(unittest.TestCase):

    def test_one(self):
        self.assertEqual(beautiful_text("Look at this example of a correct text", 5, 15), True)
    def test_two(self):    
        self.assertEqual(beautiful_text("abc def ghi", 4, 10), False)
    def test_three(self):
        self.assertEqual(beautiful_text("a a a a a a a a", 1, 10), True)
    def test_four(self):
        self.assertEqual(beautiful_text("ab cd fg xyz", 1, 5), False)
    def test_five(self):
        self.assertEqual(beautiful_text("aa aa aaaaa aaaaa aaaaa", 6, 11), True)

        