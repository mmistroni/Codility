def golden_max_slice(A):
    max_ending = A[0]
    max_slice = A[0]
    for a in A[1:]:

        max_ending = max(a, max_ending + a)
        max_slice = max(max_slice, max_ending)
    return max_slice


def solution(A):
    return golden_max_slice(A)