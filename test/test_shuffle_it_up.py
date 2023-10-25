import unittest

from shuffle_it_up import solution
from itertools import permutations, combinations

#https://math.stackexchange.com/questions/3261261/specific-position-restricted-permutation-i-dont-exactly-know-the-name-of-thi

def factorial(n, acc):
    if n == 1:
        return acc
    return factorial(n-1, acc * n)


def perm(length):
    return factorial(length, 1) / factorial(length - length, 1)


class MyTestCase(unittest.TestCase):

    def test_factorial(self):
        self.assertEqual(120, factorial(5, 1))
        self.assertEqual(4*3*2*1, factorial(4, 1))
        self.assertEqual(6 * 5 * 4 * 3 * 2 * 1, factorial(6, 1))

    def test_perms(self):
        # here's the catch
        # for each permutation the elements have to be in different position from
        # the starting point
        # Need to rethink
        # each element can only be in 3 other positions
        # so if we start with 1,2,3,4
        # 1. can be at position 2,3,4
        # 2. can be at position 1,3,4
        # 3  can be at position 1,2, 4
        # 4  can be at position 1,2,3
        ## so we need to figure out hwo to do it
        ''' heres sequence for solution
        [1, 2, 3, 4] fix
      (2, 1, 4, 3)   when 2 is first, we have so for each row we have  (n-1) + perm(3,3)
      (2, 3, 4, 1)
      (2, 4, 1, 3)
      (3, 1, 4, 2)
      (3, 4, 1, 2)
      (3, 4, 2, 1)
      (4, 1, 2, 3)
      (4, 3, 1, 2)
      (4, 3, 2, 1)
        '''

    def print_perms(self, start):
        idx = 0
        holder = []
        for i in permutations(start, len(start)):
            rest = [i - j for i, j in zip(start, i)]
            if 0 not in rest:
                holder.append(i)
        return holder

    def test_sampler(self):
        '''
        You're on the right track thinking about recursive algorithms and your deductions so far are almost correct.
        If permutations(5) is made up of (5-1) == 4 branches as you say, each having 11 leaves,
        how might we derive that number 11? You say it's permutation(n-1) - <something>
        but permutations(5-1) == permutations(4) == 9 as you say, which is smaller than 11... so something is being added, not subtracted.

        perm(1) = 0 branches       (0)
        perm(2) = 1 branch  * 0  (1)0 +
        perm(3) = 2 branches * 1 (2)
        perm(4) = 3 branches * 3  (9)
        perm(5) = 4 branches * 11 ( 44) (2+9)
        perm(6) = 5 branches * 53  (265) (44+9)
        perm(7) = 6 branches * 309 (1854)  265 + 44
        perm(8) = 7 branches * 2119 (14833) (1854 + 265)
        perm(9) =  8 branches * 16687 (133496)
        perm(10 =  9 branches * 148329  (1334961)
        perm(11) = 10 branches* 1468457  (14684570)
        perm(12) = 11 branches * 16019531 (29369141)

        :return:
        '''
        for end in [1,2, 3, 4,5,6, 7, 8, 9, 10, 11, 12]:
            start = list(range(1, end+1))
            res = self.print_perms(start)
            from pprint import pprint
            print(f'----------{end}------')
            print(f'list of {len(start)} has {len(res)} perms')
            #pprint(res)
            print(f'{len([i for i in res if i[0] == 5])}')

    def test_something(self):
        self.assertEqual(solution(1), 0)
        self.assertEqual(solution(4), 9)
        #self.assertEqual(solution(30), 97581073836835777732377428235481)

    def test_solution1(self):
        res = solution(4)
        self.assertEquals(res, 9)


    def test_solution(self):
        res = solution(30)
        self.assertEquals(res, 97581073836835777732377428235481)


if __name__ == '__main__':
    unittest.main()
