import unittest

from fib_frog import solution
import heapq
import time
from itertools import product, combinations_with_replacement


import timeit
from collections import defaultdict

'''
Few Hints
There are some stuffs that we should pay attention to:

- the frog can get to the other side of the river (from position −1 to position N), therefore the real length of the way is N + 1.
- The frog can jump over any distance F(K), where F(K) is the K-th Fibonacci number 
 means to reach position ith, the frog could go from positions (i — F(K)) where i — F(K) ≥ 0 and there is a leave at the position i — F(K).
- there are many leaves on the river, and the frog can jump between the leaves, 
   thus there are some immediate positions are not permitted.
The goal is to count the minimum number of jumps, so OPT(n) = min(1 + OPT(n — F[K]))


https://medium.com/architectalgos/mastering-the-two-pointer-technique-a-guide-to-solving-array-problems-efficiently-71bd5a22bedc
# Sign u for Leetcode
'''




class MyTestCase(unittest.TestCase):


    def test_newtest2(self):
        print('---- NEXT --')
        A = [1, 1, 0, 0, 0]
        res = solution(A)
        self.assertEquals(2, res)

    def test_single(self):
        print('---- NEXT --')
        A = [1]
        res = solution(A)
        self.assertEquals(1, res)


    def test_fibfrog(self):
        #The frog can jump over any distance F(K), where F(K) is the K-th Fibonacci number.
        A = [1, 1, 1]#[0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0]
        res = solution(A)
        self.assertEquals(2, res)

    def test_fibfrog_1(self):
        A = [0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0]
        res = solution(A)
        self.assertEquals(3, res)


    def test_fibfrog2(self):
        A = []
        jumps = solution(A)
        #res = self.probe(A)
        #res = solution(A)

        self.assertEquals(1, jumps)

    def test_fibfrog3(self):
        A = [1]
        jumps = solution(A)
        self.assertEquals(1, jumps)

    def test_fibfrog4(self):
        A = [1, 1, 1]
        res = solution(A)
        self.assertEquals(2, res)

    def test_zeros(self):
        A = [0, 0, 0]
        jumps = solution(A)
        self.assertEquals(-1, jumps)

    def test_anotherfail(self):
        A =  [0, 0, 0, 1, 0]
        jumps = solution(A) #solution(A)
        self.assertEquals(-1, jumps)

    def test_anotheranotherfail(self):
        A = [1, 1, 0, 0, 0]

        res = solution(A)
        self.assertEquals(2, res)
        #https://www.geeksforgeeks.org/python-program-for-dijkstras-shortest-path-algorithm-greedy-algo-7/


if __name__ == '__main__':
    unittest.main()
