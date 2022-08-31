import itertools
#https://app.codility.com/programmers/lessons/5-prefix_sums/passing_cars/
from collections import deque
def solution(A):
    zeros = []
    # we need to track the zeros
    passing_counter = 0
    for idx, item in enumerate(A):
        if item == 0:
            zeros.append(idx)
        else:
            passing_counter += len(zeros)
            if passing_counter > 1000000000:
                return -1

    return passing_counter

