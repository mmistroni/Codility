from collections import Counter
#https://app.codility.com/programmers/lessons/8-leader/equi_leader/

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



def solution( A):
    holder = []
    for i in range(1, len(A)):
        first = A[0:i]
        # Refactor. We jsut need to find the leader in the first.
        # once we find leader in first, we count the element on second
        second = A[i:]
        l1 = _gl2(first)
        tester = second.count(l1)

        l2 = l1 if tester > (len(second) //2)  else -1
        if l1 == l2 and l1 !=-1:
            holder.append(1)


    return len(holder)

