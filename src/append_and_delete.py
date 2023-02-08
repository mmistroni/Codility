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


def solution(s, t, k):
    if s == t:
        return 'Yes'
    elif len(s) > len(t):
        return delete(s, t, k)
    elif len(s) > len(t):
        return append_and_delete()


