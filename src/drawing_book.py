#https://www.hackerrank.com/challenges/drawing-book/problem?utm_campaign=challenge-recommendation&utm_medium=email&utm_source=24-hour-campaign

def from_start(start, p,  counter):
    pass
def from_end(start, p, counter):
    pass

def solution(n, p):



   # Need to check. if n is odd  and p == n-1 return 2
   # think we need to go with w hile loop

    if p == n or p == 1:
        return 0

    s_steps = p // 2

    e_steps = (n -p) // 2

    return min(s_steps, e_steps)