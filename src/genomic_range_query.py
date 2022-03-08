# https://app.codility.com/programmers/lessons/5-prefix_sums/genomic_range_query/

MAP_DICT = dict(A=1,C=2,G=3, T=4)

def prefix_sums(A):
    n = len(A)
    P = [0] * (n + 1)
    for k in range(1, n + 1):
        P[k] = P[k - 1] + A[k - 1]
    return P

MAP_DICT = dict(A=1,C=2,G=3, T=4)

def compute_factors(S, start_idx, end_idx):
    return sorted([MAP_DICT[item] for item in S[start_idx:end_idx]], key=lambda x:x)[0]


def solution(S, P, Q):
    return [compute_factors(S, one, two+1) for one, two in zip(P, Q)]

