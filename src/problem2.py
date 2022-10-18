import copy
def compute_all_locs(input_arr, n_locs):
    days = 0
    for item in input_arr:
        days +=1
        if item in n_locs:
            n_locs.remove(item)
        if not n_locs:
            break
    return days



def solution(A):
    unique_locs = set(A)
    holder = []
    for idx in range(0, len(A)):
        copied = copy.copy(unique_locs)
        subset = A[idx:]
        if len(subset) < len(copied):
            break
        res = compute_all_locs(subset, copied)
        holder.append(res)
    return min(holder)