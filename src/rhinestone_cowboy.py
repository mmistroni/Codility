# https://www.codewars.com/kata/58a2a561f749ed763c00000b
import re

def _find(boot):
    lines = boot.split('\n')
    counter = 0
    pattern = r"\(1\)"
    for line in lines:
        if '&' in line:
            break
        clearline = line.replace(' ', '')
        if re.search(pattern, clearline):
            counter +=1
    return counter

def cowboys_dollars(boots):
    left, right = boots

    left_dollars = _find(left)
    right_dollars = _find(right)

    return f'This Rhinestone Cowboy has {right_dollars} dollar bills in his right boot and {left_dollars} in the left'


