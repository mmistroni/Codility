#https://app.codility.com/programmers/lessons/10-prime_and_composite_numbers/flags/
# A peak is an array element which is larger than its neighbours.
# More precisely, it is an index P such that 0 < P < N − 1 and A[P − 1] < A[P] > A[P + 1].
from collections import namedtuple
def solution(N):
    peaks = []
    start_idx = None
    peak_idx = None
    for idx in range(0, len(N)-1):
        if start_idx is None:
            start_idx = idx
        else:
            current = N[idx]
            if N[start_idx] < N[idx] > N[idx+1]:
                peaks.append(idx)
                start_idx = idx+1
            else:
                if N[idx] > N[start_idx]:
                    continue
    return peaks


