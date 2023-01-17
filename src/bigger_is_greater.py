#https://www.hackerrank.com/challenges/bigger-is-greater/problem?isFullScreen=true
from itertools import combinations, permutations

from string import ascii_lowercase

def get_all_combos(word):
    holder = []
    for item in combinations(list(word), len(word)):
        holder.append(''.join(item))

    return sorted(holder, key=lambda x:x)

def solution(w):
    found = False
    for i in permutations(list(w), len(w)):
        x = ''.join(i)
        if found:
            return x
        if x == w:
            found= True
    return "no answer"

