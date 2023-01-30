#https://www.hackerrank.com/challenges/kaprekar-numbers/problem?isFullScreen=false&h_r=next-challenge&h_v=zen

import math

def is_kaprekar2(num):
    b = 10
    p = 2
    beta = (num ** 2) % b ** p
    alpha = ((num ** 2) - beta) / b ** p

    return (alpha + beta) == num


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
    res =  [i for i in range(p, q+1) if is_kaprekar(i)]
    return res