from src.twisted_sum import compute_sum
import unittest

class MyTestCase(unittest.TestCase):

    def test_test(self):
        assert compute_sum(1) == 1


    def test_one(self):
        self.assertEqual(compute_sum(1), 1)
    
    def test_two(self):
        self.assertEqual(compute_sum(2), 3)
    def test_three(self):
        self.assertEqual(compute_sum(3), 6)

    def test_four(self):    
       self.assertEqual(compute_sum(4), 10)
    
    def test_five(self):
        self.assertEqual(compute_sum(10), 46)
    def test_six(self):
        self.assertEqual(compute_sum(12), 51)
