import unittest

from chocolates_by_numbers import solution

def gcd(a, b, res, holder):
  if a == b:
    return res * a
  elif (a % 2 == 0) and (b % 2 == 0):
    holder.append(1)

    return gcd(a // 2, b // 2, 2 * res,  holder)
  elif (a % 2 == 0):
    holder.append(1)
    return gcd(a // 2, b, res, holder)
  elif (b % 2 == 0):
    holder.append(1)
    return gcd(a, b // 2, res, holder)
  elif a > b:
    holder.append(1)
    return gcd(a - b, b, res, holder)
  else:
    holder.append(1)
    return gcd(a, b - a, res, holder)



class MyTestCase(unittest.TestCase):


    def test_gcd(self):
        N, M = 10, 4
        holder = []
        res= gcd(N ,M, 0,  holder)
        print(len(holder))
        


    def test_something(self):
        N, M = 10, 4
        expected = len([0, 4, 8, 2, 6])
        res = solution(N, M)
        self.assertEqual(expected, res)


    def test_large2(self):
        N = (3 ** 9) * (2 ** 14)
        M = (2 ** 14) * (2 ** 14)

        holder = []
        res = gcd(N, M, 0, holder)
        print(len(holder))

if __name__ == '__main__':
    unittest.main()
