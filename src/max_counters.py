#https://app.codility.com/programmers/lessons/4-counting_elements/max_counters/
'''

A non-empty array A of M integers is given. This array represents consecutive operations:

if A[K] = X, such that 1 ≤ X ≤ N, then operation K is increase(X),
if A[K] = N + 1 then operation K is max counter.


'''

def solution(N, A):
    holder = [0] * N

    maxCount = 0
    for item in A:
        if 1 <= item <= N:
            holder[item-1] += 1
            maxCount = max(maxCount, holder[item-1])
        else:
            holder = [maxCount] * N


    return holder