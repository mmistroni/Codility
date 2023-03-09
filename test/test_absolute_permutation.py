import unittest

from absolute_permutation import solution
from itertools import permutations



class MyTestCase(unittest.TestCase):

    def find_permutations_for_idx(self, idx, input, k):

        # find all perms
        perms = [p for p in permutations(input, 2) if idx in p and abs(p[0] - p[1]) == k]

        #  take out of the input what we have just used
        one, two = perms[0]

        to_remove = one if two == idx else one

        return perms, input


    def test_find_right_permutation(self):
        n = 10
        k = 1

        lst = list(range(1, n+1))

        holder = []
        for idx in range(1, n + 1 ):
            tpls, lst = self.find_permutations_for_idx(idx, lst, k)
            holder.append(tpls)

        print(holder)






    def test_something(self):
        n = 4
        k = 2
        x = list(range(1, n+1))

        expected = [3, 4, 1, 2]
        self.assertEqual(expected, solution(n, k))

    def test_something2(self):
        n = 2
        k = 1
        expected = [2, 1]
        self.assertEqual(expected, solution(n, k))

    def test_something3(self):
        n = 3
        k = 0
        expected = [1, 2, 3]
        self.assertEqual(expected, solution(n, k))

    def test_something4(self):
        n = 3
        k = 2
        expected = [-1]
        self.assertEqual(expected, solution(n, k))

    def test_something5(self):
        n = 10
        k = 0
        expected = list(range(1,11))
        self.assertEqual(expected, solution(n, k))

    def test_something6(self):
        n = 10
        k = 1
        expected = [2, 1, 4, 3, 6, 5, 8, 7, 10, 9]
        self.assertEqual(expected, solution(n, k))

        '''
                1     2    3    4    5      6     7    8     9    10 
                |pos[i]- i| =  1
               2     2-1     3-2     4-3      5-4      6-5      7-6      8-7     9-8    10-9
                
        
        '''


        ''''
        inputs
        10 0
10 1
7 0
10 9
9 0
10 3
8 2
8 0
7 0
10 1
        
        outputs
        1 2 3 4 5 6 7 8 9 10
2 1 4 3 6 5 8 7 10 9
1 2 3 4 5 6 7
-1
1 2 3 4 5 6 7 8 9
-1
3 4 1 2 7 8 5 6
1 2 3 4 5 6 7 8
1 2 3 4 5 6 7
2 1 4 3 6 5 8 7 10 9
        
        
        '''







if __name__ == '__main__':
    unittest.main()
