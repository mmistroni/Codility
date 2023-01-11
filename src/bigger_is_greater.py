#https://www.hackerrank.com/challenges/bigger-is-greater/problem?isFullScreen=true

def solution(w):

    mapped = [ord(c) for c in w]

    for idx in range(len(mapped)-1, -1, -1):
        if idx > 0:
            cur = mapped[idx]
            nxt = mapped[idx-1]
            if cur > nxt:
                mapped[idx] = nxt
                mapped[idx-1] = cur
                return ''.join([chr(n) for n in mapped])

    return "no answer"