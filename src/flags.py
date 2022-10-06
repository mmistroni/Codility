#https://app.codility.com/programmers/lessons/10-prime_and_composite_numbers/flags/
# A peak is an array element which is larger than its neighbours.
# More precisely, it is an index P such that 0 < P < N − 1 and A[P − 1] < A[P] > A[P + 1].
from collections import namedtuple
def solution(N):
    peaks = []
    bottom =  (N[0], 0)
    for idx, item in enumerate(N[1:-1]):
        if N[idx-1] < N[idx] > N[idx+1]:
            peaks.append((idx, item, bottom[1]))
            bottom = (N[idx+1], idx+1)
        elif N[idx] < N[idx-1]:
            # we have a bottom
            bottom =  (N[idx], idx)
        else:
            # nothing to do
            continue

    return peaks


