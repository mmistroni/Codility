from collections import Counter
#https://app.codility.com/programmers/lessons/9-maximum_slice_problem/max_profit/

def _generateLeader(A):

    from collections import defaultdict
    if len(A) == 1:
        return A[0]
    holder = defaultdict(list)
    for idx, item  in enumerate(A):
        holder[item].append(idx)
    tp = sorted(holder.items(), key=lambda tpl: len(tpl[1]), reverse=True)
    top = tp[0]
    if len(top[1]) > len(A) / 2:
        return top[0]
    return -1

def _gl2(A):
    n = len(A)
    leader = -1
    A.sort()
    candidate = A[n // 2]
    count = 0
    for i in range(n):
        if (A[i] == candidate):
            count += 1
    if (count > n // 2):
        leader = candidate
    return leader

def golden_max_slice(A):
    max_ending = max_slice = 0
    for idx, a in enumerate(A):
        max_ending = max(0, max_ending + a)
        max_slice = max(max_slice, max_ending)
        print(f'a:{a}, maxEnding:{max_ending}, Max slice:{max_slice}')
    return max_slice

def solution( A):
    return golden_max_slice(A)
    import itertools
    combinations = itertools.combinations(A, 2)
    mx = 0
    for tpl in combinations:
        if tpl[0] > tpl[1]:
            continue
        diff = tpl[1] - tpl[0]
        if diff > mx:
            mx = diff
    return mx