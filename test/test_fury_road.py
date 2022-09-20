import unittest
'''
Examples:

1. Given R = "ASAASS", your function should return 115. 
You ride on the scooter over the first four segments ("ASAA") in 5 + 40 + 5 + 5 = 55 
and then you go on foot through "SS" in 30 + 30 = 60. 
Altogether, your journey will take 55 + 60 = 115.

2. Given R = "SSA", the function should return 80. 
You do not ride on the scooter at all, and you go on foot in 30 + 30 + 20 = 80.

3. Given R = "SSSSAAA", the function should return 175. 
You ride on the scooter all the time in 40 + 40 + 40 + 40 + 5 + 5 + 5 = 175.



'''

from fury_road import solution

class MyTestCase(unittest.TestCase):
    def test_one(self):
        R = "ASAASS"
        self.assertEqual(115, solution(R))

    def test_two(self):
        R = "SSA"
        self.assertEqual(80, solution(R))

    def test_three(self):
        R = "SSSSAAA"
        self.assertEqual(175, solution(R))


if __name__ == '__main__':
    unittest.main()
