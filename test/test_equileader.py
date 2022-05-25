import unittest
from src.equileader import solution

#https://app.codility.com/programmers/lessons/8-leader/equi_leader/
'''
A non-empty array A consisting of N integers is given.

The leader of this array is the value that occurs in more than half of the elements of A.

An equi leader is an index S such that 0 ≤ S < N − 1 and two sequences A[0], A[1], ..., A[S] and A[S + 1], A[S + 2], ..., A[N − 1] have leaders of the same value.

For example, given array A such that:

    A[0] = 4
    A[1] = 3
    A[2] = 4
    A[3] = 4
    A[4] = 4
    A[5] = 2
    '''
class MyTestCase(unittest.TestCase):
    def test_something(self):
        A = [4, 3, 4, 4, 4, 2]
        self.assertEquals(2, solution(A))

    def test_broken(self):
        A= [1, 2, 3, 4, 5]
        self.assertEqual(0, solution(A))



if __name__ == '__main__':
    unittest.main()
