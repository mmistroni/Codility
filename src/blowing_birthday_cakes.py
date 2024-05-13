#https://www.codewars.com/kata/6630da20f925eb3007c5a498

def _check(lst) :
    return sum(lst) == 0

def _decrease(lst):
    ## we need to recurse
    copied = lst
    # No this will not work
    # we need to know where the zero is  so taht
    # we can start to blow from there

    if sum(lst[0:3]) == 0:
        start = copied.index(0)

    else:
        start = 0
    end = start +3
    for idx in range(start, end):
        if copied[idx] > 0:
            copied[idx] -=1
    return copied

def blow_candles(st):
    toint = [int(s) for s in st]

    st = toint
    count = 0

    while sum(st) != 0:
        st = _decrease(st)
        count += 1

    return count

