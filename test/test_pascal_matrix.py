from src.pascal_matrix import pascal_matrix
import unittest

class MyTestCase(unittest.TestCase):
    sample_test_cases = [
        ('Simple example',
         ['DOWN', 'REPTILE', 'AMIDST', 'SOFA'],  # words
         ['DOWN', 'REPTILE', 'AMIDST', 'SOFA'],  # expected
         ),
        ('Example',
         ['DOWN', 'PLANE', 'AMIDST', 'REPTILE', 'SOFA', 'SOLAR', 'SILENCE', 'DOWN', 'MARKDOWN'],  # words
         ['DOWN', 'REPTILE', 'AMIDST', 'SOFA', 'SOLAR', 'PLANE', 'SILENCE', 'MARKDOWN'],  # expected
         ),
        ('Empty',
         [],  # words
         [],  # expected
         ),
    ]


    def test_one(self):
        res = pascal_matrix(3)
        expected = [
                        [0,1,0], 
                        [1,0,1]
                    ]

        self.assertEqual(expected, res)

    def test_two(self):
        expected = [
         [0,0,1,0,0], 
         [0,1,0,1,0], 
         [1,0,2,0,1]]
        res = pascal_matrix(5)
        self.assertEqual(expected, res)

    def test_three(self):
        res = pascal_matrix(9)
        expected = [
            [0,0,0,0,1,0,0,0,0], 
            [0,0,0,1,0,1,0,0,0], 
            [0,0,1,0,2,0,1,0,0], 
            [0,1,0,3,0,3,0,1,0], 
            [1,0,4,0,6,0,4,0,1]
            ]
        self.assertEqual(expected, res)

    def test_build_matrix(self):
        import math
        from itertools import combinations
        #  https://en.wikipedia.org/wiki/Pascal_matrix

        def binomial_coefficient(n, k):
            return math.comb(n, k)
        
        for  i in range (0,3):
            for j in range(0,3):
                print(f'({i}, {j})= {binomial_coefficient(i,j)}')
        
    # Let's start to build a pascal triangle
    def build_pascal_triangle(self, numrows):
        # i need an array of array
        

        global_arr = []
        for i in range(0, numrows):
                if i == 0:
                    global_arr.append([1])
                else:
                    curr = [0] * (i+1)
                    for j in range(len(curr)):
                        # need to sort out indexes 
                        prev_row, prev_col, next_col =  i-1, j-1, j 
                        prev_array = global_arr[prev_row]
                        left, right = 0,0
                        if prev_col < 0:
                            left = 0
                        else:
                            left = prev_array[prev_col]
                        if next_col < len(prev_array):
                            right = prev_array[next_col]
                        else:
                            right = 0
                        curr[j] = left + right
                    global_arr.append(curr)
        return global_arr               
                            
    def to_matrix(self, n, arr):
        newholder = []
        for item in arr:
            extra = n-len(item)
            refactored = item + [0] * extra
            newholder.append(refactored)

        return newholder

    def test_triangle(self):
        n = 5
        res = self.build_pascal_triangle(n)
        from pprint import pprint
        refactored = self.to_matrix(n, res)
        for item in refactored:
            print(item)







