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