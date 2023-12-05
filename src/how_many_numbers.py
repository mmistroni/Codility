# https://www.codewars.com/kata/55f5efd21ad2b48895000040
from itertools import dropwhile, filterfalse


def is_above_sum(n, max):
    str_arr = [int(i) for i in str(n)]
    return sum(str_arr) > max


def sampler(end, maxsum):

    ### forge thte filter false
    ### we start with bruteforce loop ,and we add this code
    '''
    x = "123456"
    rem = len(x) % 4
    combis = []
    for i in range(0, rem+1):
        combis.append(x[i:i+4])

    res = [is_above_sum(n) for n in combis]
    if all(res):
        holder.append(x)


    :param end:
    :param maxsum:
    :return:
    '''


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