#https://www.hackerrank.com/challenges/drawing-book/problem?utm_campaign=challenge-recommendation&utm_medium=email&utm_source=24-hour-campaign

def from_start(start, p,  counter):
    if start >= p:
        return counter
    return from_start(start + 2, p, counter + 1)

def from_end(start, p, counter):
    if p == start or p ==  start-1:
        return counter
    return from_end( start - 2, p, counter+1)

def solution(n, p):

    # Use while loop instead/ mayb instead of while loop we divide by 2

    if p == n or p == 1:
        return 0

    s =  from_start(1, p, 0)
    e =  from_end(n, p, 0)

    res =  min(s, e)

    print(f"N:{n}, P:{p}, res:{res}")
    return res