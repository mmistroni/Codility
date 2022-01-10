'''
An industrial company ha sN factories,, each producing some pollution and has decided
to reduce is total fumes bny equipping some of htem with filters
Every suchfilter reduces the pollution of a factory by half.
When a second filter is applied it  again reduces by half hte remaining pollution
For example, a factory that produces 6 unit of pollution will generate 1.5 units with 2 filters
and 0.75 with three
You are given a function, which  given an array of N integers dsecribing the amount of pollution
Your task is to find the minimun numbners of iltgers needed to reduce pollution by half
Below are the usecsaes
'''

from itertools import product
from math import exp
from pprint import pprint

def install_filters(A):
    # removing zeros, they don tcount
    A = [n for n in A if n > 0]

    res = list(product(range(0, len(A)+1), repeat=len(A)))
    filtered = [tpl for tpl in res if sum(tpl) <= 4]

    result = []
    for idx, tpl in enumerate(filtered):
        x1, x2, x3, x4 = tpl
        fun = (19 * 0.5 ** x1) + (8 * .5 ** x2) + (5 * .5 ** x3) + (2 * .5 ** x4)  #to standardize
        result.append((tpl, fun))

    good_ones = [tpl for tpl in result if tpl[1] <= 16.5]
    sorted_tpls = sorted(good_ones, key=lambda t: sum(t[0]))

    print(sorted_tpls)
    return sum([i for i in sorted_tpls[0][0]])

