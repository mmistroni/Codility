#https://www.codewars.com/kata/58552bdb68b034a1a80001fb

def cook_pancakes(n, m):
    '''
    You need to cook pancakes, but you are very hungry.
    As known, one needs to fry a pancake one minute on each side.
    What is the minimum time you need to cook n pancakes,
    if you can put on the frying pan only m pancakes at a time?
    n and m are positive integers between 1 and 1000.
    # catch: so u need 2m x slot of pancakes as you are putting them at the same
    # time on a pan
    # so n pankakes takes 2m plus 2m for remainder

    :param n:
    :param m:
    :return:
    '''

    if n < m:
        nums = 1
    else:
        nums = n // m

    return 2 * nums
