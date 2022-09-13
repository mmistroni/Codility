from itertools import combinations,dropwhile

def check(p, q, r):
    return (p + q) > r and \
    (q + r) > p and \
    (r + p) > q

def _generate_result(s_a):
    for i in range(0, len(s_a)):
        if i+2 >= len(s_a):
            break
        p = s_a[i]
        q = s_a[i + 1]
        r = s_a[i + 2]
        if check(p, q, r):
            return 1
    return 0

def solution(A):
    if len(A) < 3:
        return 0
    sorted_array = sorted(A, key=lambda x:x)

    return _generate_result(sorted_array)