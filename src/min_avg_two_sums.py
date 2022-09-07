

def prefix_sums(A):
    n = len(A)
    P = [0] * (n + 1)
    for k in range(1, n + 1):
        P[k] = P[k - 1] + A[k - 1]
    return P


def solution(A):
    holder = []
    min_idx = 0
    min_sum = sum(A[0:1])
    for i in range(0, len(A)-1):
        new_array = prefix_sums(A[i:])
        mapped = [item / idx for idx, item in enumerate(new_array) if idx > 1 ]
        minval = min(mapped)
        if minval < min_sum:
            min_sum = minval
            min_idx = i
    #    holder.append()
    #sorted_holder = sorted(holder, key=lambda tpl:tpl[1])
    return min_idx #sorted_holder[0][0]


def solution2(A):
    from itertools import combinations

    return prefix_sums(A)

