# https://app.codility.com/programmers/lessons/5-prefix_sums/genomic_range_query/

MAP_DICT = dict(A=1,C=2,G=3, T=4)

def prefix_sums(A):
    n = len(A)
    P = [0] * (n + 1)
    for k in range(1, n + 1):
        P[k] = P[k - 1] + A[k - 1]
    return P

def map_to_array(S):
    return [MAP_DICT[item] for item in S]


def solution(S):
    A = map_to_array(S)
    return 0