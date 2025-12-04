import unittest
from src.vowel_recognition import vowel_recognition

class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(vowel_recognition("bbbb"), 0)

    def test_something2(self):
        self.assertEqual(vowel_recognition("baceb"), 16)

    def test_something3(self):
        self.assertEqual(vowel_recognition("aeiou"), 35)

    def test_something4(self):
        self.assertEqual(vowel_recognition("aeiouAEIOU"), 220)    


if __name__ == '__main__':
    unittest.main()
