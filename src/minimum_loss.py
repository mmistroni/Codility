# https://www.hackerrank.com/challenges/minimum-loss/problem?isFullScreen=true
from itertools import combinations
def solution(price):
    cs =  combinations(price, 2)

    # combis not good enough.

    minloss  = None
    for s,e in cs:
        if s < e:
            continue

        if minloss is None:
            minloss = s - e
        else:
            minloss = min(minloss, s - e)
    return minloss