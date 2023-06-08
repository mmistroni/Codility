#https://app.codility.com/programmers/lessons/12-euclidean_algorithm/chocolates_by_numbers/
import logging
# https://www.researchgate.net/post/What-is-the-recurrence-relation-for-the-Euclidean-GCD-Algorithm
#https://www.hackerearth.com/practice/notes/euclid-algorithm-made-easy-1/#:~:text=There%20is%20a%20recurrence%20relation%20of%20the%20function,the%20base%20case%20is%20GCD%20%28a%2C0%29%20%3D%20a%3B

#https://www.researchgate.net/post/What-is-the-recurrence-relation-for-the-Euclidean-GCD-Algorithm
#https://www.cuemath.com/numbers/euclids-division-algorithm/

# Another hint https://www.britannica.com/science/number-theory/Euclid

def gcd(a, b, res, holder):
  if a in holder: # b and res are unique, but a is not
      return a
  holder.append(a)
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

def gcd2(N, M, start, holder):

    while True:
        if start in holder:
            return len(holder)
        else:
            holder[start] = start
            start = (start + M) % N

def gcd3(a, b, i, idx):
    while a % b != 0:
        idx += 1
        a = a + i
    return idx

def solution(N, M):
    # Not good enough, this has to do with euclidean algorithm
    # hint. use binary bcd
    ## it's supposed to run in 0.1 seconds
    return  gcd3(0+M, N,  M, 1)

