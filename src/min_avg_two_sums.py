

from prefix_sums import prefix_sums

def solution(A):
    new_array = prefix_sums(A)

    all_sums = [new_array[i]/i+1 for i in  range(1, len(new_array))]
    return [tpl for tpl in zip(new_array, all_sums)]

