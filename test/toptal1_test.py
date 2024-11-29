import unittest

from src.toptal1 import crop
class MyTestCase(unittest.TestCase):
    def test_something1(self):
        sentence = "Codility we test coders"
        K = 14
        res = crop(sentence, K)
        self.assertEqual("Codility we", res)

    def test_something2(self):
        sentence = "Why not"
        K = 100
        res = crop(sentence, K)
        self.assertEqual(sentence, res)

    def test_something3(self):
        sentence = "The quick brown fox jumps over the lazy dog"
        K = 39
        res = crop(sentence, K)
        self.assertEqual("The quick brown fox jumps over the lazy", res)

    def test_something4(self):
        sentence = "To crop or not to crop"
        K = 21
        res = crop(sentence, K)
        self.assertEqual("To crop or not to", res)




if __name__ == '__main__':
    unittest.main()
