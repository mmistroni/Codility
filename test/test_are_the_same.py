import unittest

from src.are_the_same import comp

class MyTestCase(unittest.TestCase):
    def test_one(self):
        a1 = [121, 144, 19, 161, 19, 144, 19, 11]
        a2 = [11*11, 121*121, 144*144, 19*19, 161*161, 19*19, 144*144, 19*19]
        self.assertEqual(comp(a1, a2), True)

    def test_two(self):
        a1 = [121, 144, 19, 161, 19, 144, 19, 11]
        a2 = [11*21, 121*121, 144*144, 19*19, 161*161, 19*19, 144*144, 19*19]
        self.assertEqual(comp(a1, a2), False)

    def test_three(self):
        a1 = [121, 144, 19, 161, 19, 144, 19, 11]
        a2 = [11*11, 121*121, 144*144, 190*190, 161*161, 19*19, 144*144, 19*19]



if __name__ == '__main__':
    unittest.main()
