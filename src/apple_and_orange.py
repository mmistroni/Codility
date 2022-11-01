#https://www.hackerrank.com/challenges/apple-and-orange/problem?isFullScreen=true&h_r=next-challenge&h_v=zen
def is_in_house(s, t, root, item):
    position = root + item

    if s <= position <= t:
        return 1
    return 0

def solution(s, t, a, b, apples, oranges):
    # 1. INTEGER s
    #  2. INTEGER t
    #  3. INTEGER a
    #  4. INTEGER b
    #  5. INTEGER_ARRAY apples
    #  6. INTEGER_ARRAY oranges
    apples = [is_in_house(s, t, a, item) for item in apples]
    oranges = [is_in_house(s, t, b, item) for item in oranges]
    print(f'{sum(apples)}\n{sum(oranges)}')

