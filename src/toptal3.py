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
    A = [n for n in A]

    res = list(product(range(0, len(A)+1), repeat=len(A)))
    filtered = [tpl for tpl in res if sum(tpl) <= 4]

    result = []
    for idx, tpl in enumerate(filtered):
        tpls = list(zip(A, tpl))
        fun = [tpl[0] * (.5**tpl[1]) for tpl in tpls]
        result.append((tpl, sum(fun)))

    good_ones = [tpl for tpl in result if tpl[1] <= sum(A)/ 2]
    sorted_tpls = sorted(good_ones, key=lambda t: sum(t[0]))

    print(sorted_tpls)
    return sum([i for i in sorted_tpls[0][0]])

