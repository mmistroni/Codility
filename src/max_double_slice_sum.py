from itertools import combinations
def golden_max_slice(A):
    max_ending = A[0]
    max_slice = A[0]
    # https://app.codility.com/programmers/lessons/9-maximum_slice_problem/max_double_slice_sum/
    for a in A[1:]:

        max_ending = max(a, max_ending + a)
        max_slice = max(max_slice, max_ending)
    return max_slice

def calculate_sum(combi, A):
    res = []

    maxSum = -1
    for x, y, z in combi:
        first = [A[i] for i in range(x+1, y)]
        second =[A[i] for i in range(y+1, z)]
        best = sum(first) + sum(second)
        if best > maxSum:
            maxSum = best
    return maxSum

def solution(A):
    combis =  combinations(range(0, len(A)), 3)#Sgolden_max_slice(A)
    return calculate_sum(combis, A)
