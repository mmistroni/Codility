#https://app.codility.com/programmers/lessons/12-euclidean_algorithm/chocolates_by_numbers/
import logging
# https://www.researchgate.net/post/What-is-the-recurrence-relation-for-the-Euclidean-GCD-Algorithm
#https://www.hackerearth.com/practice/notes/euclid-algorithm-made-easy-1/#:~:text=There%20is%20a%20recurrence%20relation%20of%20the%20function,the%20base%20case%20is%20GCD%20%28a%2C0%29%20%3D%20a%3B

#https://www.researchgate.net/post/What-is-the-recurrence-relation-for-the-Euclidean-GCD-Algorithm
#https://www.cuemath.com/numbers/euclids-division-algorithm/

# Another hint https://www.britannica.com/science/number-theory/Euclid
def _lcm(a, b):
    return a * b / (_gcd(a,b))

def _gcd(a, b):
    print('in gcd')
    if a % b == 0:
        return b
    else:
        return _gcd(b, a % b)



def solution(N, M):
    # Not good enough, this has to do with euclidean algorithm
    # hint. use binary bcd
    ## it's supposed to run in 0.1 seconds
    lcm_res = _lcm(N, M)
    return lcm_res / M

