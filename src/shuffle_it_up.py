#https://www.codewars.com/kata/5b997b066c77d521880001bd/train/python
from itertools import permutations

def print_perms(start):
    idx = 0
    for i in permutations(start, len(start)):
        rest = [i - j for i, j in zip(start, i)]
        if 0 not in rest:
            idx += 1
    return idx

def solution(array_length):
    lst =  list(range(1, array_length + 1))
    res = print_perms(lst)
    return res