from itertools import count
from collections import Counter
def solution(A):
    dt = Counter(A)
    for n in count(start=1):
        if n not in dt.keys():
            return n



