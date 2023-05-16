#https://app.codility.com/programmers/lessons/12-euclidean_algorithm/chocolates_by_numbers/
import logging
# https://www.researchgate.net/post/What-is-the-recurrence-relation-for-the-Euclidean-GCD-Algorithm
#https://www.hackerearth.com/practice/notes/euclid-algorithm-made-easy-1/#:~:text=There%20is%20a%20recurrence%20relation%20of%20the%20function,the%20base%20case%20is%20GCD%20%28a%2C0%29%20%3D%20a%3B

#https://www.researchgate.net/post/What-is-the-recurrence-relation-for-the-Euclidean-GCD-Algorithm


#https://www.cuemath.com/numbers/euclids-division-algorithm/

def gcd(a, b, res, holder):
  if a in holder:
      return b
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


def solution(N, M):
    # Not good enough, this has to do with euclidean algorithm
    # hint. use binary bcd
    ## it's supposed to run in 0.1 seconds
    holder = []
    return gcd(M, N, 1, holder)
