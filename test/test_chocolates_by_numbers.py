import unittest

from chocolates_by_numbers import solution

def gcd(a, b, res, holder):
  if a in holder: # b and res are unique, but a is not
      return len(holder)
  else:
      holder.append(1)
  if a == b:
    return res * a
  elif (a % 2 == 0) and (b % 2 == 0):
    return gcd(a // 2, b // 2, 2 * res,  holder)
  elif (a % 2 == 0):
    return gcd(a // 2, b, res, holder)
  elif (b % 2 == 0):
    return gcd(a, b // 2, res, holder)
  elif a > b:
    return gcd(a - b, b, res, holder)
  else:
    return gcd(a, b - a, res, holder)



class MyTestCase(unittest.TestCase):


    def test_gcd(self):
        N, M = 10, 4
        holder = []
        res= gcd(M, N, 1,  holder)
        self.assertEqual(5, res)
        


    def test_something(self):
        N, M = 10, 4
        expected = 5
        res = solution(N, M)
        self.assertEqual(expected, res)


    def test_small(self):
        N, M = 24, 18
        res = gcd(N, M, 1, [])
        self.assertEqual(4, res)


    def test_large1(self):
        N = (3 ** 9) * (2 ** 14)
        M = (2 ** 14) * (2 ** 14)
        holder = []
        res = gcd(M, N, M, holder)
        self.assertEqual(19684, res)

    def test_large2(self):
        N = (3 ** 9) * (2 ** 14)
        M = (2 ** 14) * (2 ** 14)

        holder = []
        res =solution(N, M)
        self.assertEquals(19684, res)


if __name__ == '__main__':
    unittest.main()
