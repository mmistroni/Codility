#https://www.codewars.com/kata/526d84b98f428f14a60008da/train/python
from heapq import heapify, heappop, heapreplace, heappush


# https://en.wikipedia.org/wiki/Regular_number#:~:text=In%20computer%20science%2C%20regular%20numbers%20are%20often%20called,used%20as%20a%20test%20case%20for%20functional%20programming.
from heapq import heapify, heappop, heapreplace


def get_nth_hamming_number(n):
    """
    This function finds the nth Hamming number using the modified Fibonacci approach.
    Args:
        n: The index of the desired Hamming number.
    Returns:
        The nth Hamming number.
    """
    h = [1]
    p2, p3, p5 = 0, 0, 0
    for _ in range(n - 1):
        next_num = min(2 * h[p2], 3 * h[p3], 5 * h[p5])
        h.append(next_num)
        if next_num % 2 == 0:
            p2 += 1
        if next_num % 3 == 0:
            p3 += 1
        if next_num % 5 == 0:
            p5 += 1
    return h[-1]


def hamming(n):
    return get_nth_hamming_number(n)
