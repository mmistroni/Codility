import unittest

from src.how_many_numbers import max_sumDig, is_above_sum

'''
We want to find the numbers higher or equal than 1000 that the sum of every four consecutives digits cannot be higher than a certain given value. 
If the number is num = d1d2d3d4d5d6, and the maximum sum of 4 contiguous digits is maxSum, th

max_sumDig(2000, 3) -------> [11, 1110, 12555]

(1) -There are 11 found numbers: 1000, 1001, 1002, 1010, 1011, 1020, 1100, 1101, 1110, 1200 and 2000

(2) - The mean of all the found numbers is:
      (1000 + 1001 + 1002 + 1010 + 1011 + 1020 + 1100 + 1101 + 1110 + 1200 + 2000) /11 = 1141.36363,  
      so 1110 is the number that is closest to that mean value.

(3) - 12555 is the sum of all the found numbers
      1000 + 1001 + 1002 + 1010 + 1011 + 1020 + 1100 + 1101 + 1110 + 1200 + 2000 = 12555

Finally, let's see another cases

max_sumDig(2000, 4) -----> [21, 1120, 23665]

max_sumDig(2000, 7) -----> [85, 1200, 99986]

max_sumDig(3000, 7) -----> [141, 1600, 220756]



'''
from itertools import dropwhile, filterfalse

class MyTestCase(unittest.TestCase):


    def sampler(self, end, maxsum):
        return max_sumDig(end, maxsum)

    def test_sampler(self):
        res = self.sampler(2000, 3)
        print(*res)

    def tester(self):
        holds= []

        x = filterfalse(lambda l: is_above_sum(l, 9), range(1000, 82426))
        for n in x:
            holds.append(n)

        print(f'HOlder has :{len(holds)}')
        from pprint import pprint


    def test_ias(self):
        self.assertTrue(self.is_above_sum(1033, 3))
        self.assertFalse(self.is_above_sum(1020, 3))
    def test_one(self):
        res = self.sampler(2000 , 3)
        self.assertEqual([11, 1110, 12555], res)
    def test_two(self):
        res = self.sampler(2000 , 4)
        self.assertEqual([21, 1120, 23665], res)

    def test_three(self):
        res = self.sampler(2000 , 7)
        self.assertEqual([85, 1200, 99986], res)

    def test_four(self):
        res = self.sampler(3000 , 7)
        self.assertEqual([141, 1600, 220756], res)

    def test_failure(self):
        res = self.sampler(82426, 9)
        self.assertEqual(res, [3059, 27000, 81510822])


if __name__ == '__main__':
    unittest.main()
