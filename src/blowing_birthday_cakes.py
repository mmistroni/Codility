#https://www.codewars.com/kata/6630da20f925eb3007c5a498

def _check(lst) :
    return sum(lst) == 0

def _decrease(lst , counter, zero_idx):
    ## we need to recurse
    ## we can only look ahead 3
    ## Current setup does not work.
    ## we need to be able to detect if we
    ## start with a zero 
    ##
    ## lets try
    start = max(0, counter)
    end = min(counter + 3, len(lst))
    if sum(lst[counter:min(counter+3, len(lst))]) > 0:
        for i in range(start, end):
            if lst[i] > 0:
                lst[i] -=1
        return lst, counter
    else:
        counter = counter + 3
        return _decrease(lst, counter, zero_idx)


def blow_candles(st):
    toint = [int(s) for s in st]

    st = toint
    count = 0


    counter = 0
    rounds = 0
    while sum(st) != 0:
        st, counter = _decrease(st, counter, rounds)
        print('Running another loop')
        count += 1

    return count

