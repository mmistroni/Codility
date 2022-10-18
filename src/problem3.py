
def _mean(A):
    if not A:
        return 0
    if isinstance(A, int):
        return A
    return sum(A) / len(A)

def solution(A, S):
    times = 0
    for idx in range(0, len(A) ):
        first = A[0:idx]
        second = A[idx:]

        if _mean(first)  == S:
            times +=1
        if _mean(second) == S:
            times +=1
    return times



    # write your code in Python 3.8.10
