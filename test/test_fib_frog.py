import unittest

from src.fib_frog import solution
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
# learn yield keywords
'''
import sys

def generate_fib_steps(n):
    a, b = 1, 1
    yield 1
    while a + b <= n:
        yield a + b
        a, b = b, a + b


def solutionA(A):
    n = len(A) + 1

    ret = [sys.maxsize] * (n + 1)
    ret[0] = 0

    for i in range(1, n + 1):
        # so we
        if (i < n and A[i - 1] == 1) or (i == n):
            ret[i] = min([ret[i - x] + 1 for x in generate_fib_steps(i)])
            #aha. so we  mark as 1  in ret then by increasing i, we check if i - (FIB) is another 1.
            # good idea! WE STILL need to elaborate
            print(f'i:{i}, ret:{ret}')
        else:
            print(f'{i} is no goods')

    return ret[-1] if ret[-1] < sys.maxsize else -1


class MyTestCase(unittest.TestCase):

    def test_sol(self):
        A = [0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0]
        res = solutionA(A)
    def test_newtest2(self):
        print('---- NEXT --')
        A = [0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0]

        '''
          # Start with -1
          # get all the steps that can get us to ones including end
          # then we loop thru those and do the same
          # 
        
        
        
        '''




        def generate_steps(idx, end, A):
            for f in generate_fib_steps(end-idx):
                nxt = start + f
                if A[nxt] == 1:
                    return nxt
            return -1


        # start from -1
        # get next fib
        # increment idx and see if A[i] ==1
        start = -1
        end  = len(A) + 1
        ''' pseudocode
            # we have the speedy fibonacci
            # starting from idx, we get all fib numbers that from start leads to the next no
            # if we get the algo for the first one, then we get it for everything
        '''
        counter = 0

        for idx in range(0, len(A)+1):
            if A[idx] == 0:
                continue
            else:
                k = generate_steps(start, idx, A)
                if k > 0:
                    generate_steps(idx,k)


        print(f'We needed:{counter} steps')

    def test_new_fib(self):
        for f in generate_fib_steps(100):
            print(f)

    def test_single(self):
        print('---- NEXT --')
        A = [1]
        res = solution(A)
        self.assertEquals(1, res)


    def test_fibfrog(self):
        #The frog can jump over any distance F(K), where F(K) is the K-th Fibonacci number.
        A = [1, 1, 1]#[0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0]
        res = solutionA(A)
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
