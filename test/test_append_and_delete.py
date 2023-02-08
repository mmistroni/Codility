import unittest

from append_and_delete import solution

class MyTestCase(unittest.TestCase):
    def test_something(self):
        s = 'abc'
        t = 'def'
        k = 6
        self.assertEqual('Yes', solution(s, t, k))

    def test_something2(self):
        s = 'hackerhappy'
        t = 'hackerank'
        k = 9
        self.assertEqual('Yes', solution(s, t, k))

    def test_something3(self):
        s = 'aba'
        t = 'aba'
        k = 7
        self.assertEqual('Yes', solution(s, t, k))

    def test_something4(self):
        s = 'ashley'
        t = 'ash'
        k = 2
        self.assertEqual('No', solution(s, t, k))




if __name__ == '__main__':
    unittest.main()
