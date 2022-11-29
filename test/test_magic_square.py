import unittest

from magic_square import solution
import numpy as np

class MyTestCase(unittest.TestCase):
    def test_something(self):
        input = [[5, 3, 4], [1, 5, 8], [6, 4, 2]]
        res = solution(input)
        self.assertEqual(True, False)

    def test_combi(self):
        input = [[5, 3, 4], [1, 5, 8], [6, 4, 2]]

        a = np.array(input)

        print(f'Matrix:{a}')
        for i in range(0,3):
            col = a[:,i]
            row = a[i, :]
            print(f'{i}-Row:{row}')
            print(f'{i}- Col:{col}')

        ## Perhaps use numpy  matrixes?



if __name__ == '__main__':
    unittest.main()
