# https://www.hackerrank.com/challenges/kangaroo/problem?isFullScreen=true
def solution(x1, v1, x2, v2):

    pos1 = x1
    pos2 = x2
    while pos1 <= pos2:
        pos1 += v1
        pos2 += v2
        if pos1 == pos2:
            return "YES"
        if pos2 > pos1 and v2 >= v1:
            return "NO"

    return "NO"