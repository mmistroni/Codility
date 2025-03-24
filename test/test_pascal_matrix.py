from src.pascal_matrix import pascal_matrix
import unittest


def modified_pascal_matrix(n):
    """
    Generates a modified Pascal's triangle with zeros inserted, for generic Pascal matrix.

    Args:
      n: The number of rows to generate.

    Returns:
      A list of lists representing the modified Pascal's triangle.
    """
    if n <= 0:
        return []

    triangle = []
    if n >= 1:
        triangle.append([0, 1, 0])
    if n >= 2:
        triangle.append([1, 0, 1])

    for i in range(2, n):
        prev_row = triangle[i - 1]
        new_row = []
        pascal_row = [1] * (i + 1)

        for j in range(1, i):
            # Boundary checks to prevent IndexError
            left = prev_row[2 * (j - 1) + 1] if 2 * (j - 1) + 1 < len(prev_row) else 0
            right = prev_row[2 * j + 1] if 2 * j + 1 < len(prev_row) else 0
            pascal_row[j] = left + right

        for val in pascal_row:
            new_row.append(val)
            new_row.append(0)

        new_row.pop()
        triangle.append(new_row)

    return triangle

def pascal_triangle(n):
    """
    Calculates Pascal's triangle up to row n.

    Args:
        n: The number of rows to generate.

    Returns:
        A list of lists representing Pascal's triangle.
    """
    if n <= 0:
        return []

    triangle = []
    for i in range(n):
        row = [1] * (i + 1)  # Initialize row with 1s
        if i > 1:
            for j in range(1, i):
                row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
        triangle.append(row)
    return triangle

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


    def modified_pascal_matrix(self, n):
        """
        Generates a modified Pascal's triangle with zeros inserted, for generic Pascal matrix.

        Args:
            n: The number of rows to generate.

        Returns:
            A list of lists representing the modified Pascal's triangle.
        """
        if n <= 0:
            return []

        triangle = []

        for i in range(n):
            if i == 0:
                triangle.append([0, 1, 0])
                continue

            prev_row = triangle[i - 1]
            new_row = []
            pascal_row = [1] * (i + 1)

            if i > 1:
                for j in range(1, i):
                    # Calculate Pascal's triangle values from the *previous* modified row
                    pascal_row[j] = prev_row[2 * (j - 1) + 1] + prev_row[2 * j + 1]

            for val in pascal_row:
                new_row.append(val)
                new_row.append(0)
            
            new_row.pop() #remove the last zero.
            triangle.append(new_row)

        return triangle





    def test_triangle(self):
        #print(modified_pascal_matrix(3))
        #print(modified_pascal_matrix(5))
        #print(modified_pascal_matrix(9))
        # we start fromm this to figure out how many element sin last row
        # and from this we can generate the triangle
        for i in [3,5,9]:
            print(f'-------------------- {i} ---------------------')
            print(self.count_nonzero_elements(i))



        #res = self.modified_pascal_matrix(n)
        #print(res)
        
        ''' 
            we need to figure out the link between pascal triangle and pascal matrix
            2^n.


            pascalMatrix(3) =
                    [[0,1,0], 
                    [1,0,1]]
                        so this is the matrix for pascal(2)
            pascalMatrix(5) =

                [[0,0,1,0,0], 
                [0,1,0,1,0], 
                [1,0,2,0,1]]
                this is the matrix for pascal(3)

                
            pasalMatrix(9)
                [[0,0,0,0,1,0,0,0,0],
                [0,0,0,1,0,1,0,0,0],
                [0,0,1,0,2,0,1,0,0],
                [0,1,0,3,0,3,0,1,0],
                [1,0,4,0,6,0,4,0,1]]
                this is the matrix for pascal(5)                            
        
        
        '''


        #from pprint import pprint
        #refactored = self.insert_zeros_respecting_length(res)
        #refactored = self.to_matrix(n, res)
        #for item in refactored:
        #    print(item)

    def count_nonzero_elements(self, last_row_elements):
        """
        Calculates the number of non-zero elements in a row where zeros are inserted 
        between every other number.

        Args:
            last_row_elements: The total number of elements in the last row.

        Returns:
            The number of non-zero elements.
        """
        if last_row_elements <= 0:
            return 0

        return (last_row_elements + 1) // 2





