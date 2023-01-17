#https://www.hackerrank.com/challenges/bigger-is-greater/problem?isFullScreen=true
from itertools import combinations

from string import ascii_lowercase

def get_all_combos(word):
    holder = []
    for item in combinations(list(word), len(word)):
        holder.append(''.join(item))

    return sorted(holder, key=lambda x:x)

def solution(w):

    items = get_all_combos(w)

    if len(set(items)) == 1:
        return "no answer"

    idx = items.index(w)
    return items[idx+1]

