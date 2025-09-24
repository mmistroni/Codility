import unittest
import logging
from src.chocolates_by_numbers import solution

'''
24, 18   gcd = 6

- 0 % 18 = 0

1 - 0 +18 %24  = 18

2 - 18 + 18  % 24  = 12

3 - 12 + 18 % 24 = 6 (gcd)

4 - 6 + 18 % 24 = 0      6 is the gcd between 18 and 24





10, 4  gcd = 2


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

def gcd(a, b, res, idx):
    idx+=1
    print(f'a:{a}, b:{b}, res:{res}')
    if a <= b:
        print(f'We should get out at:{idx}')
    if a == b:
        return res * a
    elif (a % 2 == 0) and (b % 2 == 0):
        return gcd(a // 2, b // 2, 2 * res, idx)
    elif (a % 2 == 0):
        return gcd(a // 2, b, res, idx)
    elif (b % 2 == 0):
        return gcd(a, b // 2, res, idx)
    elif a > b:
        return gcd(a - b, b, res, idx)
    else:
        return gcd(a, b - a, res, idx)


def gcd3(a, b, i, idx):
    if a % b == 0:
        return idx
    else:
        idx += 1
        return gcd3(a+i,  b, i, idx)

def lcm(a, b):
    return a * b / (_gcd(a,b))

def _gcd(a, b):
    print('in gcd')
    if a % b == 0:
        return b
    else:
        return _gcd(b, a % b)


class MyTestCase(unittest.TestCase):


    def test_exercise(self):
        N, M = 10, 4
        lcm_res = lcm(N,M)
        # expected 5
        gcd_res = _gcd(N, M)

        print(f'({N},{M}) LCM:{lcm_res}, GCD:{gcd_res}')

    def test_exercise2(self):
        N, M = 24, 18
        lcm_res = lcm(N,M)
        # expected 4
        gcd_res = _gcd(N, M)

        print(f'({N},{M}) LCM:{lcm_res}, GCD:{gcd_res}')



    def test__gcd(self):
        N, M = 10, 4
        expected = 5
        holder = []
        res= _gcd(N,  M)
        l = lcm(N, M)

        print(f'GCD:{res}, LCM:{l}')

    def test__gcd2(self):
        N, M = 24, 18
        expected = 4
        holder = []

        res= _gcd(N,  M)
        l = lcm(N, M)

        print(f'GCD:{res}, LCM:{l}')


    def test_something(self):
        N, M = 10, 4
        expected = 5
        res = solution(N, M)
        #(10,4) LCM:20.0, GCD:2

        self.assertEqual(expected, res)

    def test_something2(self):
        N, M = 24, 18
        expected = 4
        # (24,18) LCM:72.0, GCD:6
        res = solution(N, M)
        self.assertEqual(expected, res)

        #self.assertEqual(4, res)


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
