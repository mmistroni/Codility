#https://www.hackerrank.com/challenges/absolute-permutation/problem?isFullScreen=true

def solution(n , k):
    # Need a lexicographically permutation. see test/test_bigger_is_greater.py. oor mayb not
    # we loop from 0 to len(n) and check if there is an elem
    # then we find the lexicograhically smallest

    # we need to go down prm route. for ever idx find permutation taht results in [pos[i] - i] = k

    lst = list(range(1, n+1))

    if k == 0:
        return lst


    holder = []
    for i in range(1, n+1):
        #  is considered to be an absolute permutation if [pos[i] - i| =k  holds true for every  pos[i]. = k + i
        candidate = k + i



        if candidate in lst:
            lst.pop(candidate)
            holder.append(candidate)
        else:
            return [-1]
    return holder




