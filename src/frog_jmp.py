from math import ceil
def jump(start, end , span, counter=0):

    res = (end - start) / span
    return int(ceil(res))



