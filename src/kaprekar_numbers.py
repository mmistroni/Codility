#https://www.hackerrank.com/challenges/kaprekar-numbers/problem?isFullScreen=false&h_r=next-challenge&h_v=zen

import math


def is_kaprekar(num):
    squared = str(num ** 2)

    if len(squared) >= 2:
        mid_point = len(squared) // 2
        summed = int(squared[0:mid_point]) + int(squared[mid_point:])
        return summed == num
    else:
        return int(squared) == num
    return False
def solution(p, q):
    return [i for i in range(p, q) if is_kaprekar(i)]

