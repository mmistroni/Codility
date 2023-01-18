import unittest

from bigger_is_greater import solution

class MyTestCase(unittest.TestCase):


    def test_something(self):
        res = solution('ab')
        self.assertEqual('ba', res)


    def test_something2(self):
        res = solution('bb')
        self.assertEqual('no answer', res)

    def test_something3(self):
        res = solution('hefg')
        self.assertEqual('hegf', res)

    def test_something4(self):
        res = solution('dhck')
        self.assertEqual('dhkc', res)

    def test_something5(self):
        res = solution('dkhc')
        self.assertEqual('hcdk', res)

    def test_something6(self):
        res = solution('abcd')
        self.assertEqual('abdc', res)

    def test_something7(self):
        res = solution('dcbb')
        self.assertEqual('no answer', res)


if __name__ == '__main__':
    unittest.main()
