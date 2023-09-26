import unittest

from fibonacci_ladder import solution
import heapq
import time
from itertools import product, combinations_with_replacement

#https://proofwiki.org/wiki/Properties_of_Fibonacci_Numbers#Millin_Series

import timeit
from collections import defaultdict

def fibonacci_seq(n, limit=None):
    fib = [0] * (n+2)
    fib[1] = 1
    for i in range(2, n+1):
        if i == limit:
            break
        fib[i] = fib[i-1] + fib[i-2]

    return [f for f in fib if f > 0 and f < limit]


class MyTestCase(unittest.TestCase):

    '''
    1
    2
    3
    4


    '''



    def test_newtest2(self):
        print('---- NEXT --')
        A = [4,4,5,5,1]
        B = [3,2,4,3,1]

        for item in A:
            # We need to change this. we are not looking for sum but to see
            # if we are at rung 4
            current_seq = fibonacci_seq(item, item)
            res = []
            for cl in range(1, item+1):
                for p in product(current_seq, repeat=cl):
                    if p[0] in [1,2] and sum(p) == item:
                        if not p in res:
                            res.append(p)

            # We need to try to eliminate number 3, which screws up
            # all the calculations
            # Mayb we try another way. We first find all the numbers
            # you can jump to and see if these are fibonacci

            '''
            1   
          2     3
        3   4  4   5
      4   5   6       5
      
     # what we need to do is to build a fibonacci tree until we get to the destination
     
     
       1
     2     3
   3   4  4  5
  4 

        #sCRAP. 
        check this https://dev.to/alisabaj/the-climbing-staircase-problem-how-to-solve-it-and-why-the-fibonacci-numbers-are-relevant-3c4o
        Test it out. sample only shows 4 and 5 ladder
        
        1 step
        2 step
        3 step
        4 step
        5 step 
        6 step
        7 step
      '''


            print(f'For {item} we have found {res} way')

            print(f'{item}={current_seq}')

        return

        expected = [5, 1, 8, 0, 1]

        # so you can start from rung (k) 1 or 2, and you can  only
        #  move up via k+1 or k+2



        # explanation: for N=4 there are
        '''
        For example, given N = 4, you have five different ways of climbing, ascending by:

            1, 1, 1 and 1 rung,
            1, 1 and 2 rungs,
            1, 2 and 1 rung,
            2, 1 and 1 rungs, and
            2 and 2 rungs
        
            Given N = 5, you have eight different ways of climbing, ascending by:

                1, 1, 1, 1 and 1 rung,
                1, 1, 1 and 2 rungs,
                1, 1, 2 and 1 rung,
                1, 2, 1 and 1 rung,
                1, 2 and 2 rungs,
                2, 1, 1 and 1 rungs,
                2, 1 and 2 rungs, and
                2, 2 and 1 rung.
    
            Idx   A  B   sol      
            0     4   3   5 % 2^3 = 5   
            1     4   2   5 % 2^2 = 1
            2     5   4   8 % 2^4 = 8
            3     5   3   8 % 2^3 = 0
            4     1   1   1 % 2 ^1 = 1
               
            
            
            
        '''


        res = solution(A)
        self.assertEquals(2, res)





if __name__ == '__main__':
    unittest.main()
