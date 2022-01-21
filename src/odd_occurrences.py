from collections import Counter
def solution(A):
    c = Counter(A)
    return [k for k, v in c.items() if v % 2 ==1][0]


