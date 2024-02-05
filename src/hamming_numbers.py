#https://www.codewars.com/kata/526d84b98f428f14a60008da/train/python
from heapq import heapify, heappop, heapreplace, heappush


# https://en.wikipedia.org/wiki/Regular_number#:~:text=In%20computer%20science%2C%20regular%20numbers%20are%20often%20called,used%20as%20a%20test%20case%20for%20functional%20programming.
from heapq import heapify, heappop, heapreplace

def _hamming(n):
    x = []
    setter = set()
    setter.add(1)
    heapify(x)
    heappush(x, 1)
    cur = 0
    for i in range(1, n + 1):
        cur = heappop(x)  # We dont remove..we need to keep so we can get item
        heappush(x, cur * 2)
        heappush(x, cur * 3)
        heappush(x, cur * 5)
        setter.add(cur * 2)
        setter.add(cur * 3)
        setter.add(cur * 5)

    return list(setter)


def hamming(n):
    res = _hamming(n)
    print(f'Penultiamte is:{res[-1]}')
    return res[n-1]