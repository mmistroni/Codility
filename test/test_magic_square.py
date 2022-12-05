import unittest

from magic_square import solution
import numpy as np

class MyTestCase(unittest.TestCase):
    def test_something(self):
        input = [[5, 3, 4], [1, 5, 8], [6, 4, 2]]
        res = solution(input)
        print(f'Result is {res}')
        self.assertEqual(True, True)

    def test_combi(self):

        first = np.matrix([2,9,4],
                          [7,5,3],
                          [6,1,8])
        first_ = np.matrix([6,1,8],
                          [7,5,3],
                          [2, 9,4])
        first__ = np.matrix([4, 9, 2],
                            [3, 5, 7],
                            [8, 1, 6])

        # rotate clockwise
        r1 = np.matrix([6, 7, 2],  # first row is first col
                       [1, 5, 9],  # second row is second col
                       [8, 3, 4])  # third row is third col
                                   # we could use transpose
        r2 = np.matrix([8, 1, 6],
                       [3, 5, 7],
                       [4, 9, 2])

        r3 = np.matrix([4, 3, 8],
                       [9, 5, 1],
                       [2, 7, 6])

        # rotate anticlockwise
        r4 = np.matrix([2, 7, 6],
                       [9, 5, 1],
                       [4, 3, 8])


        # Then we swap first col and last col and rotate



if __name__ == '__main__':
    unittest.main()
