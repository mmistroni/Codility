import unittest

from chocolates_by_numbers import solution

def gcd(a, b, res):
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



class MyTestCase(unittest.TestCase):


    def test_gcd(self):
        N, M = 10, 4
        res= gcd(N ,M, N % M)
        print(res)


    def test_something(self):
        N, M = 10, 4
        expected = len([0, 4, 8, 2, 6])
        res = solution(N, M)
        self.assertEqual(expected, res)


    def test_large2(self):
        N = (3 ** 9) * (2 ** 14)
        M = (2 ** 14) * (2 ** 14)
        res = solution(N, M)

if __name__ == '__main__':
    unittest.main()
