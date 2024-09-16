#https://www.codewars.com/kata/62ad72443809a4006998218a

from enum import Enum
#from preloaded import Like, Dislike, Nothing
from functools import reduce


class Test(Enum):
    Like  = 1,
    Dislike = 2.
    Nothing = 3

def choose(last, current):
    if last == current:
        return Test.Nothing
    else:
        return current


def like_or_dislike(lst):
    if not lst:
        return Test.Nothing

    res = reduce(lambda acc, item: choose(acc, item), lst[1:], lst[0] )

    return res
