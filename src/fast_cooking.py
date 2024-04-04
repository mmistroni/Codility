#https://www.codewars.com/kata/58552bdb68b034a1a80001fb

def cook_pancakes(n, m):
    '''
    You need to cook pancakes, but you are very hungry.
    As known, one needs to fry a pancake one minute on each side.
    What is the minimum time you need to cook n pancakes,
    if you can put on the frying pan only m pancakes at a time?
    n and m are positive integers between 1 and 1000.

    # so if you have more than m pans, then you can flip some of them
    Let's try this out
    n = 3, m = 2

    if n > m you can swap what you have left with one in the pan
    but let'see
    if the difference is only 1, then it'll take 2m + 1

    if the difference is 2, let's see
    n = 5, m = 3

    1 will take 2 m
    2 swap out
    so it'll take 3 m






    # catch: so u need 2m x slot of pancakes as you are putting them at the same
    # time on a pan
    # so n pankakes takes 2m plus 2m for remainder

    # not yet there. we'll need to figure out exactly how many extra minutes
    # we need when we have pancakes in excess

    :param n:
    :param m:
    :return:
    '''

    nums = 0
    rem = 0

    if n < m:
        nums = 1
        rem = 0
    else:
        if n % m == 0:
            nums = n // m
        else:
            nums = n // m
            rem =1


    # m pancakes takes 2 minutes because they cook together
    # plus you need 2 mins for remainder


    return 2 * nums  + rem
