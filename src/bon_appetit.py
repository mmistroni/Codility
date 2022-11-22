# https://www.hackerrank.com/challenges/bon-appetit/problem?isFullScreen=true
def solution(bill, k, b):
    '''
    bill: an array of integers representing the cost of each item ordered
    k: an integer representing the zero-based index of the item Anna doesn't eat
    b: the amount of money that Anna contributed to the bill

    '''
    bill.pop(k)
    anna_sum = sum(bill) / 2

    if anna_sum == b:
        return 'Bon Appetit'
    return f'{int(b - anna_sum)}'
