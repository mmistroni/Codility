#https://www.codewars.com/kata/6630da20f925eb3007c5a498

def _check(lst) :
    return all([(i == 0) for i in lst])

def _decrease(lst):
    # not right
    if 0 in lst:
        idx = lst.index(0)
    else:
        idx = -1
    bound1, bound2 = idx +1, idx + 4

    #need better
    new_array = [item-1 if bound1 <= idx < bound2 and item > 0 else item for idx, item in enumerate(lst) ]

    return new_array


def blow_candles(st):
    toint = [int(s) for s in st]

    st = toint
    count = 0

    while not _check(st):
        count +=1
        st = _decrease(st)

    return count

