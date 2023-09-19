import unittest

from fibonacci_ladder import solution
import heapq
import time
from itertools import product, combinations_with_replacement


import timeit
from collections import defaultdict

def fibonacci_seq(n, limit=None):
    fib = [0] * (n+2)
    fib[1] = 1
    for i in range(2, n+1):
        fib[i] = fib[i-1] + fib[i-2]
        if fib[i] >= limit:
             break

    return [f for f in fib if f > 0 and f < limit]


class MyTestCase(unittest.TestCase):





    def test_newtest2(self):
        print('---- NEXT --')
        A = [4,4,5,5,1]
        B = [3,2,4,3,1]

        for item in A:
            current_seq = fibonacci_seq(item, item)
            res = []
            for cl in range(1, item+1):
                for p in product(current_seq, repeat=cl):
                    if p[0] in [1,2] and sum(p) == item:
                        if not p in res:
                            res.append(p)
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
