# https://app.codility.com/programmers/lessons/3-time_complexity/tape_equilibrium/
import math
def solution(A):
    total = sum(A)
    cs = None
    start = A[0]
    for i in range(1, len(A)):
        first = start
        last = total - first
        dff = abs(first - last)
        cs = dff if cs is None else min(cs, dff)
        start = start + A[i]
    return cs