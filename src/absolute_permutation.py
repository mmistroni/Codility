#https://www.hackerrank.com/challenges/absolute-permutation/problem?isFullScreen=true

def solution(n , k):
    # Need a lexicographically permutation. see test/test_bigger_is_greater.py. oor mayb not
    # we loop from 0 to len(n) and check if there is an elem
    lst = list(range(1, n+1))
    holder = []
    for i in range(1, n+1):
        #  is considered to be an absolute permutation if [pos[i] - i| =k  holds true for every  pos[i]. = k + i
        candidate = k + i if i <= k else i -k
        if candidate in lst:
            holder.append(candidate)
        else:
            return [-1]
    return holder




