import unittest

from src.fast_cooking import cook_pancakes

class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEquals(cook_pancakes(1, 2), 2)

    def test_something2(self):
        self.assertEquals(cook_pancakes(2, 2), 2)

    def test_something3(self):
        self.assertEquals(cook_pancakes(4, 2), 4)

    def test_something4(self):
        self.assertEquals(cook_pancakes(3, 2), 3)

    def test_something5(self):
        self.assertEquals(cook_pancakes(4, 3), 3)

    def test_something6(self):
        self.assertEquals(cook_pancakes(941, 165), 12)

    def test_something7(self):
        self.assertEquals(cook_pancakes(598, 128),  10)

    def test_something8(self):
        self.assertEquals(cook_pancakes(700, 241),  6)

    def test_something9(self):
        self.assertEquals(cook_pancakes(500, 173), 6)

    def test_something10(self):
        self.assertEquals(cook_pancakes(966, 381), 6)

    def test_something11(self):
        self.assertEquals(cook_pancakes(798, 555), 3)

    def test_something12(self):
        self.assertEquals(cook_pancakes(728, 545) , 3)

    def test_something13(self):
        self.assertEquals(cook_pancakes(525, 47) , 23)

    def test_something14(self):
        self.assertEquals(cook_pancakes(989, 106) , 19)



if __name__ == '__main__':
    unittest.main()
