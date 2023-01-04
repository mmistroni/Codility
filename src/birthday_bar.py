#https://www.hackerrank.com/challenges/the-birthday-bar/problem?isFullScreen=true
from itertools import combinations

def find_segments(s, length):
    holders = []
    for i in range(0, len(s)):
        to_go = len(s) - i
        if to_go < length:
            break
        valid_seg = s[i:i+length]
        holders.append(valid_seg)
    return holders


def solution(s, d, m):
    '''

    :param s: segment
    :param d: day of birth
    :param m: month of birth
    :return:
    '''
    avail_segs = find_segments(s, m)
    good_ones =[s for s in avail_segs if sum(s) == d]
    return len(good_ones)
