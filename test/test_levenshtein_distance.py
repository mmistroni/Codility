import unittest
from levenshtein_distance import levenshtein

class MyTestCase(unittest.TestCase):

    def test_one(self):
        self.assertEqual(levenshtein("kitten", "sitting"), 3)

    def test_two(self):
        self.assertEqual(levenshtein("book", "back"), 2)

    def test_three(self):
        self.assertEqual(levenshtein("book", "book"), 0)

    def test_four(self):
        self.assertEqual(levenshtein("qlzcfayxiz", "vezkvgejzb"), 9)

    def test_five(self):
        self.assertEqual(levenshtein("nayvyedosf", "sjxen"), 9)


    def test_six(self):
        self.assertEqual(levenshtein("sjxen", "sjxen"), 0)

    def test_seven(self):
        self.assertEqual(levenshtein("peter", "peter"), 0)

    def test_eight(self):
        self.assertEqual(levenshtein("bookie", "book"), 2)

if __name__ == '__main__':
    unittest.main()
