#https://www.hackerrank.com/challenges/bigger-is-greater/problem?isFullScreen=truehttps://www.hackerrank.com/challenges/bigger-is-greater/problem?isFullScreen=true
from itertools import combinations, permutations

from string import ascii_lowercase


def next_permutation(word):

    # Find pivo2
    for k in range(len(word) - 2, -1, -1):
        if word[k] < word[k + 1]:
            break
    else:
        return word

    # find pivot successor
    for l in range(len(word) - 2, k, -1):
        if word[k] < word[l]:
            break
    # swap
    
    word[k], word[l] = word[l], word[k]

    first = word[0:k + 1]
    second = word[k + 1:]  # [::-1]

    return first + second[::-1]


def solution(w):
    lst = list(w)
    sol = next_permutation(lst)

    packaged = ''.join(sol)
    if packaged == w:
        return 'no answer'
    return packaged


