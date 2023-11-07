import unittest
from ds_multof_pfs import  solution

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

class MyTestCase(unittest.TestCase):

    def test_findfactors(self):
        tst  =12
        F = arrayF(tst)
        factors = factorization(tst, F)
        print(factors)

    def test_ten_to_hundred(self):
        expected = [12, 15, 35, 42, 60, 63, 66, 68, 84, 90, 95]
        res =  solution(10, 100)
        self.assertEquals(expected, res)

    def test_twenty_to_hundredtwenty(self):
        expected = [35, 42, 60, 63, 66, 68, 84, 90, 95, 110, 114, 119]
        res = solution(20, 120)
        self.assertEquals(expected, res)

if __name__ == '__main__':
    unittest.main()
