#https://www.codewars.com/kata/58552bdb68b034a1a80001fb

def cook_pancakes(n, m):
    # can only cook m
    # each pk requires 2m

    if n < m:
        nums = 1
    else:
        nums = n // m

    return 2 * nums

