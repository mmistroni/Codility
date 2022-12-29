import unittest

from toptal_online import countMissingTag

class MyTestCase(unittest.TestCase):

    def test_case1(self):
        res = countMissingTag("<app></app></app></app>",[],[])
        self.assertEqual(2, res)  # add assertion here

    def test_case2(self):
        res = countMissingTag("<app></app><app></app>",[],[])
        self.assertEqual(0, res)  # add assertion here


    def test_case3(self):
        res = countMissingTag("<app></app><app><app>",[],[])
        self.assertEqual(2, res)  # add assertion here


    def test_case4(self):
        res = countMissingTag("</app><app><app>",[],[])
        self.assertEqual(3, res)  # add assertion here


if __name__ == '__main__':
    unittest.main()
