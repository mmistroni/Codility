import unittest
from mrjefferson import  shortest_arrang

class MyTestCase(unittest.TestCase):

    def test_one(self):
        self.assertEquals(shortest_arrang(10), [4, 3, 2, 1])

    def test_two(self):
        self.assertEquals(shortest_arrang(14), [5, 4, 3, 2])

    def test_three(self):
        self.assertEquals(shortest_arrang(16), [-1])

    def test_four(self):
        self.assertEquals(shortest_arrang(22), [7, 6, 5, 4])

    def test_five(self):
        self.assertEquals(shortest_arrang(65), [33, 32])
