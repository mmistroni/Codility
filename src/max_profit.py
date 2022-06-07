def golden_max_slice(A):
    max_ending = max_slice = 0
    for a in A:
        if a < max_ending:
            a = -a
        max_ending = max(0, max_ending + a)
        max_slice = max(max_slice, max_ending)
    return max_slice


def solution(A):
    return golden_max_slice(A)
    n = len(A)
    result = 0
    for p in range(n-1):
        for q in range(p+1, n):
            print(f'{p}, {q}')
            gain = A[q] - A[p]
            print(f'Gain:{gain}')
            result = max(result, gain)
    return result


