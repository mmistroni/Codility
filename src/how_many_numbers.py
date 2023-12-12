# https://www.codewars.com/kata/55f5efd21ad2b48895000040
from itertools import dropwhile, filterfalse
def sum_of_digits(nstr):
    str_arr = [int(i) for i in nstr]
    return sum(str_arr)

def gather_valids(end, maxsum):
    holds = []
    for n in range(1000, end + 1):
        ndigits = str(n)
        if len(ndigits) == 4:
            sd = sum_of_digits(ndigits)
            if sd <= maxsum:
                holds.append(int(ndigits))
        else:
            rem = len(ndigits) % 4
            tpl = []
            for i in range(0, rem + 1):
                tpl.append(ndigits[i:i + 4])
            vals = [sum_of_digits(i) for i in tpl]
            res = [sd <= maxsum for sd in vals]
            if all(res):
                holds.append(int(ndigits))
    return holds

def sampler(end, maxsum):

    nums = gather_valids(end, maxsum)
    one = len(nums)
    avg = sum(nums) // len(nums)

    mindiff = None
    selected = nums[0]
    for i in range(0, len(nums) // 2):
        f = abs(nums[i] - avg)
        s = abs(nums[len(nums)-i-1] - avg)
        if not mindiff:
            mindiff = min(f, s)
        else:
            mindiff = min(mindiff, f, s)

    final1 = avg - mindiff
    final2 = avg + mindiff
    if final1 in nums:
        second = final1
    else:
        second = avg + mindiff

    three = sum(nums)

    return [one, second, three]


def max_sumDig(nMax, maxSum):
    # range(1000, nMax+1)
    return sampler(nMax, maxSum)

def solution(n):
    return 0