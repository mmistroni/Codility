# https://www.hackerrank.com/challenges/counting-valleys/problem?utm_campaign=challenge-recommendation&utm_medium=email&utm_source=24-hour-campaign

'''
A mountain is a sequence of consecutive steps above sea level,
starting with a step up from sea level and ending with a step down to sea level.
A valley is a sequence of consecutive steps below sea level,
starting with a step down from sea level and ending with a step up to sea level.

'''
SEA = 0

def find_valleys(lst):
    num_valleys = 0
    in_valley = False
    while lst:
        item = lst.pop()
        if item < 0:
            in_valley = True
        else:
            if in_valley:
                num_valleys +=1
                in_valley = False
    return num_valleys


def solution(steps, path):
    state = SEA
    mapped = []
    tolist = list(path)
    while tolist:
        step = tolist.pop(0)
        if step == "U":
            state +=1
        else:
            state -=1
        mapped.append(state)
    print(mapped)
    return find_valleys(mapped)