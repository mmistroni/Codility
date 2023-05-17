import unittest

from chocolates_by_numbers import solution

'''
24, 18

0 % 18 = 0

0 +18 %24  = 18

18 + 18  % 14  = 12

30 % 24 = 6

24 % 24 = 0



'''


def gcd2(N, M, start, holder):
    stop = False

    while True:
        if start in holder:
            return len(holder)
        else:
            holder.append(start)
            start = (start + M) % N

class MyTestCase(unittest.TestCase):


    def test_gcd(self):
        N, M = 10, 4
        holder = []
        res= gcd2(N, M, 0,  [])



    def test_something(self):
        N, M = 10, 4
        expected = 5
        res = solution(N, M)
        self.assertEqual(expected, res)


    def test_small(self):
        N, M = 24, 18
        res = solution(N, M)
        self.assertEqual(4, res)


    def test_large1(self):
        N = (3 ** 9) * (2 ** 14)
        M = (2 ** 14) * (2 ** 14)
        holder = []
        res = solution(N, M)

        print(f'Large has result:{res}')


        self.assertEqual(19683, res)

    def test_large2(self):
        N = (3 ** 9) * (2 ** 14)
        M = (2 ** 14) * (2 ** 14)

        holder = []
        res =solution(N, M)
        self.assertEquals(19684, res)


if __name__ == '__main__':
    unittest.main()
