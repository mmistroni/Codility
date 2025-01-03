import unittest

from src.absolute_permutation import solution
from itertools import permutations, chain



class MyTestCase(unittest.TestCase):

    def find_permutations_for_idx(self, idx, input, k, holder):
        reduced = input #list(set(input) - set(holder))
        perms = [p for p in permutations(reduced, 2) if idx in p]
        filtered = [p for p in perms if ( (p[0] - p[1]) == k) or ( (p[1]-p[0]) == k) ]

        tmp = set([i for i in list(chain(*filtered)) if i not in holder and
                i != idx])
        return filtered



    def find_right_permutation(self, n, k):
        # need inspiration here
        #n = 4
        #k = 2
        lst = list(range(1, n+1))
        if k == 0:
            return lst
        holder = []
        for idx in range(1, n + 1 ):
            tpls =  self.find_permutations_for_idx(idx, lst, k, holder)
            try:
                first = tpls[0]
            except Exception as e:
                return [-1]
            tmp = list(first)
            tmp.remove(idx)

            holder.append(tmp[0])

        return holder


    def test_something(self):
        n = 4
        k = 2
        x = list(range(1, n+1))

        expected = [3, 4, 1, 2]

        res = self.find_right_permutation(n, k)
        self.assertEqual(expected, res)

    def test_something2(self):
        n = 2
        k = 1
        expected = [2, 1]
        res = self.find_right_permutation(n, k)

        self.assertEqual(expected, res)

    def test_something3(self):
        n = 3
        k = 0
        expected = [1, 2, 3]
        res = self.find_right_permutation(n, k)

        self.assertEqual(expected, res)

    def test_something4(self):
        n = 3
        k = 2
        expected = [-1]
        res = self.find_right_permutation(n, k)
        self.assertEqual(expected, res)

    def test_something5(self):
        n = 10
        k = 0
        expected = list(range(1,11))
        res = self.find_right_permutation(n, k)
        self.assertEqual(expected, res)

    def test_something6(self):
        # TO follow up. 2 is used twice..
        n = 10
        k = 1
        expected = [2, 1, 4, 3, 6, 5, 8, 7, 10, 9]
        res = self.find_right_permutation(n, k)
        self.assertEqual(expected, res)

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
