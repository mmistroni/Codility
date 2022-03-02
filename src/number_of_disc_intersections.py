# check this link
# https://www.bbc.co.uk/bitesize/guides/z9pssbk/revision/4#:~:text=Two%20circles%20will%20touch%20if%20the%20distance%20between,%28d%20%3D%20%7Br_1%7D%29%20or%20%20%28d%20%3D%20%7Br_2%7D%29.
#https://app.codility.com/programmers/lessons/6-sorting/number_of_disc_intersections/
from collections import Counter
from itertools import product, combinations

def num_of_intersections(tpl1, tpl2):
    # We need some sorting here
    # case1, 1 touch
    center_distance = abs(tpl1[0] - tpl2[0])
    d_sum = tpl1[1] + tpl2[1]
    d_diff = abs(tpl1[1][1]) - tpl2[1]


def Solution(A):
    centersAndRadius = [(idx, item) for idx, item in enumerate(A)]

    for t in combinations(centersAndRadius, 2):
        print(t)


    print(centersAndRadius)
    return None









