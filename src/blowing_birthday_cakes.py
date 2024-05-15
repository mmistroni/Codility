#https://www.codewars.com/kata/6630da20f925eb3007c5a498

def _check(lst) :
    return sum(lst) == 0

def _decrease(lst , counter, zero_idx):
    ## we need to recurse
    if zero_idx < 3 and counter < len(lst):
        item = lst[counter]
        if item != 0:
            item -= 1
            lst[counter] = item
            zero_idx += 1
        counter += 1
        return _decrease(lst, counter, zero_idx)
    else:
        print(f'Exiting with {lst}')
        return lst


def blow_candles(st):
    toint = [int(s) for s in st]

    st = toint
    count = 0


    counter = 0
    rounds = 0
    while sum(st) != 0:
        st = _decrease(st, counter, rounds)
        print('Running another loop')
        count += 1

    return count

