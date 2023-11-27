import unittest

from src.how_many_numbers import solution

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


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)


if __name__ == '__main__':
    unittest.main()
