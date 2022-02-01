

from prefix_sums import prefix_sums

def solution(A):
    new_array = prefix_sums(A)

    all_sums = [new_array[i]/i for i in  range(0, new_array)]
    return all_sums

