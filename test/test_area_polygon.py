import unittest

from area_polygon import area_of_inscribed_polygon
import math


class MyTestCase(unittest.TestCase):
    def test_something1(self):
        res = area_of_inscribed_polygon(3, 3)  # returns 11.691342951089922
        self.assertTrue(math.isclose(res, 11.691342951089922, abs_tol=0.001 ))

    def test_something2(self):

        res = area_of_inscribed_polygon(5.8, 7)  # returns
        self.assertTrue(math.isclose(res, 92.05283874578583, abs_tol=0.001))

    def test_something3(self):
        res = area_of_inscribed_polygon(4, 5)
        self.assertTrue(math.isclose(res, 38.04226065180614, abs_tol=0.001))

if __name__ == '__main__':
    unittest.main()
