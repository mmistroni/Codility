#https://app.codility.com/programmers/lessons/10-prime_and_composite_numbers/flags/
# A peak is an array element which is larger than its neighbours.
# More precisely, it is an index P such that 0 < P < N − 1 and A[P − 1] < A[P] > A[P + 1].
from collections import namedtuple


def check_flag_nums(peaks, flags):
    found_flags = 0
    last_flag = 0
    for i in range(0, len(peaks)):
        if i == 0:
            found_flags += 1
            last_flag = 0
        else:
            if peaks[i] - peaks[last_flag] >= flags:
                found_flags += 1
                if found_flags > flags:
                    return flags
                last_flag = i
    return found_flags


def evaluate(peaks):
    '''
    Flags can only be set on peaks.
    What's more, if you take K flags,
    then the distance between any two flags should be greater than or equal to K.
    The distance between indices P and Q is the absolute value
    '''
    maxFlags = len(peaks)
    flags = [check_flag_nums(peaks, i) for i in range(1, maxFlags)]
    return max(flags)


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
    return evaluate(peaks)


