import unittest

from magic_square import solution
import numpy as np

class MyTestCase(unittest.TestCase):
    def test_something(self):
        magixboxes = [
            [[2, 9, 4], [7, 5, 3], [6, 1, 8]],
            [[6, 7, 2], [1, 5, 9], [8, 3, 4]],
            [[8, 1, 6], [3, 5, 7], [4, 9, 2]],
            [[4, 3, 8], [9, 5, 1], [2, 7, 6]],
            [[4, 9, 2], [3, 5, 7], [8, 1, 6]],
            [[8, 3, 4], [1, 5, 9], [6, 7, 2]],
            [[6, 1, 8], [7, 5, 3], [2, 9, 4]],
            [[2, 7, 6], [9, 5, 1], [4, 3, 8]]]

        input = [[5, 3, 4], [1, 5, 8], [6, 4, 2]]

        tmp = np.array(input)

        for idx, item in enumerate(magixboxes):
            itemarray = np.array(item)
            diffs = np.sum(itemarray - tmp)

            print(f'Item {idx} has diff={diffs}')


    def test_combi(self):

        first = np.matrix([2,9,4],
                          [7,5,3],
                          [6,1,8])
        rowswap_ = np.matrix([6,1,8],
                          [7,5,3],
                          [2, 9,4])
        colswap__ = np.matrix([4, 9, 2],
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

    def _rotate_clockwise(self, input_array):
        first_row = input_array[:,0][::-1]
        second_row = input_array[:,1][::-1]
        third_row = input_array[:, 2][::-1]
        return np.array([first_row, second_row, third_row])

    def test_generate_all_rotations(self):
        holder = []
        first = np.array([[2, 9, 4],
                          [7, 5, 3],
                          [6, 1, 8]])
        holder.append(first)
        for i in range(0,3):
            first = self._rotate_clockwise(first)
            holder.append(first)

        first_row = first[:, 0][::1]
        second_row = first[:, 1][::1]
        third_row = first[:, 2][::1]

        first = np.array([first_row,
                          second_row,
                          third_row])
        holder.append(first)
        for i in range(0,3):
            first = self._rotate_clockwise(first)
            holder.append(first)


        from pprint import pprint
        pprint(holder)


if __name__ == '__main__':
    unittest.main()
