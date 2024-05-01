import unittest

from spinning_rings import spinning_rings

class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEquals(spinning_rings(2, 3), 5)

    def test_something1(self):
        self.assertEquals(spinning_rings(3, 2), 2)

    def test_something2(self):
        self.assertEquals(spinning_rings(1, 1), 1)

    def test_something3(self):
        self.assertEquals(spinning_rings(2, 2), 3)

    def test_something4(self):
        self.assertEquals(spinning_rings(3, 3), 2)


if __name__ == '__main__':
    unittest.main()
