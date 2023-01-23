#https://www.hackerrank.com/challenges/bigger-is-greater/problem?isFullScreen=truehttps://www.hackerrank.com/challenges/bigger-is-greater/problem?isFullScreen=true
from itertools import combinations, permutations

from string import ascii_lowercase

def get_all_combos(word):
    holder = {}
    for item in permutations(list(word), len(word)): # not the right choice
        it = ''.join(item)
        holder[it] = it

    return sorted(holder.values(), key=lambda x:x)

def solution(w):
    found = False

    combos = get_all_combos(w)
    from pprint import pprint

    res = "no answer"
    for idx, item in enumerate(combos):
        if item == w:
            try:
                res = combos[idx + 1]
            except Exception as e:
                return "no answer"
    if res == w:
        return "no answer"
    return res

