import unittest
from math import sqrt
from src.ds_multof_pfs import solution, factors
from itertools import product, combinations

def arrayF(n):
    F = [0] * (n + 1)
    i = 2
    while (i * i <= n):
        if (F[i] == 0):
            k = i * i
            while (k <= n):
                if (F[k] == 0):
                    F[k] = i;
                k += i

        i += 1
    return F

def factorization(x, F):
    primeFactors = []
    while (F[x] > 0) :
        primeFactors += [F[x]]
        x //= F[x]
    primeFactors += [x]
    return primeFactors

def  printDivisors(n):
    d = []
    for i in range(1, int(sqrt(n)) + 1):
        if (n % i == 0) :

            # If divisors are equal, print only one
            if (n / i == i):
                d.append(i)
                print( i);

            else : #// Otherwise print both
                d.append(i)
                d.append(n / i)
                print(f'{i}, { n / i}')

    return [int(n) for n in d]
class MyTestCase(unittest.TestCase):
    # https://www.geeksforgeeks.org/generating-all-divisors-of-a-number-using-its-prime-factorization/

    def is_good(self, tst):
        # there should be an intersection between prime divisors and factors
        F = arrayF(tst)
        factors = factorization(tst, F)
        res = printDivisors(tst)
        return sum(res) % sum(factors) == 0



    def test_find_factorss(self):
        tst = 12
        F = arrayF(tst)
        res = factorization(tst, F)
        print(f'First round:{res}')
        f = factors(tst)
        print(f'Second round:{res}')

        self.assertEqual(res, f)



    def test_find_divsors(self):
        from collections import Counter
        from itertools import product,combinations
        tst = 12

        res = solution(12,13)

        print(res)





    def test_findfactors(self):
        # not good. we need to find out divisors out of prime factors
        # https://math-from-scratch.com/faq/104-find-divisors-of-a-number
        tst  =12
        F = arrayF(tst)
        factors = factorization(tst, F)
        res = [1] + factors + [tst]

        divs = []
        for p in combinations(res, 2):
            if p[0] * p[1] <= tst:
                x = p[0] * p[1]
                if x not in divs:
                    divs.append(x)


        print(f'Fsum:{sum(factors)}')
        print(f'DivSum:{sum(divs)}')
        print(f'-----------------s')
        res = printDivisors(tst)
        print(f'{res}, {sum(res)}')


    def test_ten_to_hundred(self):
        expected = [12, 15, 35, 42, 60, 63, 66, 68, 84, 90, 95]
        res =  solution(10, 100)
        self.assertEquals(expected, res)

    def test_twenty_to_hundredtwenty(self):
        expected = [35, 42, 60, 63, 66, 68, 84, 90, 95, 110, 114, 119]
        res = solution(20, 120)
        self.assertEquals(expected, res)

    def test_eightyfour(self):
        expected = [84]
        res =  solution(83, 85)

    def test_twelve(self):
        expected = [84]
        res =  solution(12, 13)

    def test_outoftime(self):
        import time

        start = time.time()
        res = solution(4042, 6752)
        end = time.time()
        print(end - start)


    def test_outoftime2(self):
        import time

        start = time.time()
        res = solution(4030, 6591)
        end = time.time()
        print(end - start)


if __name__ == '__main__':
    unittest.main()
