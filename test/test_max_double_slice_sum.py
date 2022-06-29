from src.max_double_slice_sum import solution
import unittest

class MyTestCase(unittest.TestCase):
    '''
    https://app.codility.com/programmers/lessons/9-maximum_slice_problem/max_double_slice_sum/

    A triplet (X, Y, Z), such that 0 ≤ X < Y < Z < N, is called a double slice.

    The sum of double slice (X, Y, Z) is the total of
    A[X + 1] + A[X + 2] + ... + A[Y − 1] + A[Y + 1] + A[Y + 2] + ... + A[Z − 1].

    For example, array A such that:

    A[0] = 3
    A[1] = 2
    A[2] = 6
    A[3] = -1
    A[4] = 4
    A[5] = 5
    A[6] = -1
    A[7] = 2
    contains the following example double slices:

    double slice (0, 3, 6), sum is 2 + 6 + 4 + 5 = 17, A[1] + A[2] + A[4] + A[5]
    double slice (0, 3, 7), sum is 2 + 6 + 4 + 5 − 1 = 16,
    double slice (3, 4, 5), sum is 0.


    '''


    def test_something(self):
        A = [3, 2, 6, -1, 4, 5, -1,  2]
        self.assertEquals(17, solution(A))


if __name__ == '__main__':
    unittest.main()
