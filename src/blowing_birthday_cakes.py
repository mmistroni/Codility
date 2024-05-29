#https://www.codewars.com/kata/6630da20f925eb3007c5a498

def _decrease(lst , counter, start_idx):
    # Not yet there. so we need to avoid loop
    # and just go from first index that is above zero to 3 max
    if sum(lst) == 0:
        return counter
    else:
        counter +=1
        end_idx = None
        found = None
        for idx, item in enumerate(lst):
            if end_idx and idx > end_idx:
                return _decrease(lst, counter, 0)
            if item > 0:
                if not found:
                    found = True
                    end_idx = idx + 2
                lst[idx] -=1
            else:
                continue
        return _decrease(lst, counter, 0)

def blow_candles(st):
    toint = [int(s) for s in st]

    st = toint

    result = _decrease(st, 0, 0)

    return result
