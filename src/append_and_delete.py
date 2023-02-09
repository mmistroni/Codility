#https://www.hackerrank.com/challenges/append-and-delete/problem

def delete(s, t, k):
    # Need to use a while loop to check

    if k == 0:
        return 'No'
    else:
        k -=1
        s = s[0 : -1]
        if s == t:
            return 'Yes'
        return delete(s, t, k)

def find_same_root(s, t, k):
    if not s:
        return '',  k
    if k == 0:
        return None, k
    else:
        s = s[0:-1]
        k -=1
        if s == t:
            return s,  k
        else:
            t = t[0:len(s)]
            if s ==t:
                return s, k
            return find_same_root(s, t, k)



def solution(s, t, k):
    if s == t:
        return 'Yes'
    else :
        s, k = find_same_root(s, t, k)

        if s is None:
            return 'No'

        remainder = len(t) - len(s)

        if k != remainder:
            return 'No'
        return 'Yes'
