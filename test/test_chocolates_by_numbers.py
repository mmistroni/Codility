import unittest
import logging
from chocolates_by_numbers import solution

'''
24, 18

- 0 % 18 = 0

1 - 0 +18 %24  = 18

2 - 18 + 18  % 24  = 12

3 - 12 + 18 % 24 = 6

4 - 6 + 18 % 24 = 0

10, 4


 0 % 10 = 0

1 0 + 4  % 10= 4

2 4 + 4  % 10 = 8

3 8 + 4  % 10 = 2

4 2 + 4  % 10 = 6

5 6 + 4 % 10 = 0


'''


def gcd2(N, M, start, holder):
    stop = False

    while True:
        if start in holder:
            return len(holder)
        else:
            holder.append(start)
            start = (start + M) % N

def gcd(a, b, res):
    print(f'a:{a}, b:{b}, res:{res}')
    if a == b:
        return res * a
    elif (a % 2 == 0) and (b % 2 == 0):
        return gcd(a // 2, b // 2, 2 * res)
    elif (a % 2 == 0):
        return gcd(a // 2, b, res)
    elif (b % 2 == 0):
        return gcd(a, b // 2, res)
    elif a > b:
        return gcd(a - b, b, res)
    else:
        return gcd(a, b - a, res)


def gcd3(a, b, i):
    print(f'a:{a}, b:{b}, i:{i}')
    if a % b == 0:
        return i
    else:
        i += 1

        return gcd3(b, a % b, i)

class MyTestCase(unittest.TestCase):


    def test_gcd(self):
        N, M = 10, 4
        holder = []
        res= gcd3(N, M, 0)
        print(f'GCD:{res}')



    def test_something(self):
        N, M = 10, 4
        expected = 5
        res = solution(N, M)
        self.assertEqual(expected, res)


    def test_small(self):
        N, M = 24, 18
        res = solution(N, M)
        print(res)
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
