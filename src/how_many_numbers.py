# https://www.codewars.com/kata/55f5efd21ad2b48895000040
from itertools import dropwhile, filterfalse


def is_above_sum(n, max):
    str_arr = [int(i) for i in str(n)]
    return sum(str_arr) > max


def sampler(end, maxsum):
    x = filterfalse(lambda x: is_above_sum(x, maxsum), range(1000, end + 1))

    nums = [n for n in x]

    one = len(nums)
    avg = sum(nums) // len(nums)
    x = dropwhile(lambda x: x >= avg, nums[::-1])
    y = dropwhile(lambda x: x <= avg, nums)
    two = next(x)
    two_other = next(y)
    d1 = abs(avg - two)
    d2 = abs(avg - two_other)

    second = two if d1 < d2 else two_other

    three = sum(nums)

    return [one, second, three]


def max_sumDig(nMax, maxSum):
    # range(1000, nMax+1)
    return sampler(nMax, maxSum)

def solution(n):
    return 0