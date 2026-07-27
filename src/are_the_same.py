# https://www.codewars.com/kata/550498447451fbbd7600041c/train/python
'''
Given two arrays a and b write a function comp(a, b) (orcompSame(a, b))
that checks whether the two arrays have the "same" elements, with the same multiplicities (the multiplicity of a member is the number of times it appears). "Same" means, here, that the elements in b are the elements in a squared, regardless of the order.
'''
from collections import Counter


def comp(array1, array2):
    if array1 is None or array2 is None:
        return False
    if len(array1) != len(array2):
        return False

    if len(array1) == 0 and len(array2) == 0:
        first_arr_counter = Counter(array1)
        for key, value in first_arr_counter.items():
            if key ** 2 not in array2 or array2.count(key ** 2) != value:
                return False
    return True




