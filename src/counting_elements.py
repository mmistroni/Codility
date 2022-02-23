def amend(arr, idx):
    arr[idx] +=1

def increase_all(A):
    return [max(A)] * len(A)

def solution(N, A):
    tmp = [0] * N

    
    for idx, item in enumerate(A):
        if item == N + 1:
            tmp = increase_all(tmp)
        else:
            amend(tmp, item-1)
    return tmp


