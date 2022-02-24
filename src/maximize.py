from functools import reduce
def find_positives(A):
    return A[-3:]

def find_negatives(A):
    # max 2
    return A[0:2]

def solution(A):

    A.sort()
    pos_list = find_positives(A)
    neg_list = find_negatives(A)
    if (neg_list[0] * neg_list[1]) > (pos_list[0] * pos_list[1]):
        neg_list.append(pos_list[-1])
        total = neg_list
    else:
        total = pos_list
    return reduce(lambda acc, item: acc * item, total, 1)


    return last_three[0] * last_three[1] * last_three[2]
