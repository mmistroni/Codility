import unittest

from shuffle_it_up import solution
from itertools import permutations, combinations
import time



#https://math.stackexchange.com/questions/3261261/specific-position-restricted-permutation-i-dont-exactly-know-the-name-of-thi

def factorial(n, acc):
    if n == 1:
        return acc
    return factorial(n-1, acc * n)


def perm(length):
    return factorial(length, 1) / factorial(length - length, 1)

'''
        You're on the right track thinking about recursive algorithms and your deductions so far are almost correct.
        If permutations(5) is made up of (5-1) == 4 branches as you say, each having 11 leaves,
        how might we derive that number 11? You say it's permutation(n-1) - <something>
        but permutations(5-1) == permutations(4) == 9 as you say, which is smaller than 11... so something is being added, not subtracted.

        perm(1) = 0 branches       (0)
        perm(2) = 1 branch  * 1  (1)0 +   (n-1) * 1
        perm(3) = 2 branches * 1 (2)   (n-1) * (perm(n-1)) + perm(n-2)
        perm(4) = 3 branches * 3  (9)   3 * (1 + 2)
        perm(5) = 4 branches * 11 ( 44) (2+9) 3
        perm(6) = 5 branches * 53  (265) (44+9)
        perm(7) = 6 branches * 309 (1854)  265 + 44
        perm(8) = 7 branches * 2119 (14833) (1854 + 265)
        perm(9) =  8 branches * 16687 (133496)
        perm(10 =  9 branches * 148329  (1334961)
        perm(11) = 10 branches* 1468457  (14684570)
        perm(12) = 11 branches * 16019531 (29369141)
'''


def pseudo_fib(n):
    # Not good. Need to cache like we did  in other fibs
    if n == 1:
        return 0
    if n == 2:
        return 1
    return (n-1) * (pseudo_fib(n-1) + pseudo_fib(n-2))


def generate_fib_steps(n):
    a, b = 0, 1
    yield 1
    while a + b <= n:
        yield a + b
        a, b = (n-1) * b, (n-1) * (a + b)

def fibonacci_seq(n, limit=None):
    fib = [0] * (n + 2)
    fib[1] = 1
    for i in range(2, n + 1):
        fib[i] =  (i) * (fib[i - 1] + fib[i - 2])
    return fib

class MyTestCase(unittest.TestCase):


    def test_pseudo_fib(self):
        for i in range(1,6):
            res = pseudo_fib(i)
            res2 = fibonacci_seq(i)
            print(f'pseudo_fib of {i}={res} vs {res2[i-1]}')

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
        perm(2) = 1 branch  * 1  (1)0 +   (n-1) * 1
        perm(3) = 2 branches * 1 (2)   (n-1) * (perm(n-1)) + perm(n-2)
        perm(4) = 3 branches * 3  (9)   3 * (1 + 2)
        perm(5) = 4 branches * 11 ( 44) (2+9) 3
        perm(6) = 5 branches * 53  (265) (44+9)
        perm(7) = 6 branches * 309 (1854)  265 + 44
        perm(8) = 7 branches * 2119 (14833) (1854 + 265)
        perm(9) =  8 branches * 16687 (133496)
        perm(10 =  9 branches * 148329  (1334961)
        perm(11) = 10 branches* 1468457  (14684570)
        perm(12) = 11 branches * 16019531 (29369141)

        :return:
        '''
        for end in [1,2, 3, 4,5]:
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


    def test_big(self):


        self.assertEqual(solution(12), 29369141)

    def test_solution1(self):
        res = solution(4)
        self.assertEquals(res, 9)


    def test_solution(self):
        start = time.time()
        res = pseudo_fib(30)
        self.assertEquals(res, 97581073836835777732377428235481)
        end = time.time()
        print(end - start)

    def test_fastsolution(self):
        n = 30
        start = time.time()
        res = solution(n)
        end = time.time()
        print(end - start)

        self.assertEquals(res, 97581073836835777732377428235481)


if __name__ == '__main__':
    unittest.main()
