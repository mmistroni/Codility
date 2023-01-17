#https://www.hackerrank.com/challenges/bigger-is-greater/problem?isFullScreen=true

def solution(x):

    w = list(x)
    for i in range(0, len(w)):
        if i < len(w)-1:
            prev = ord(w[i])
            nxt = ord(w[i+1])
            if prev > nxt:
                w[i], w[i+1] = w[i+1], w[i]
                return ''.join(w)



    return "not possible"