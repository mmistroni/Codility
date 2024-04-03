import unittest

from fast_cooking import cook_pancakes

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




if __name__ == '__main__':
    unittest.main()
