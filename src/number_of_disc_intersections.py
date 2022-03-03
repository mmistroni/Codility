# check this link
# https://www.bbc.co.uk/bitesize/guides/z9pssbk/revision/4#:~:text=Two%20circles%20will%20touch%20if%20the%20distance%20between,%28d%20%3D%20%7Br_1%7D%29%20or%20%20%28d%20%3D%20%7Br_2%7D%29.
#https://app.codility.com/programmers/lessons/6-sorting/number_of_disc_intersections/

#TODO  this needs to be improved!!
from itertools import product, combinations, permutations
def num_of_intersections(tpl1, tpl2):
    #https: // www.bbc.co.uk / bitesize / guides / z9pssbk / revision / 4

    # We need some sorting here
    # we need to see if a circle contains the other as well
    # case1, 1 touch
    center_distance = abs(tpl1[0] - tpl2[0])
    d_sum = tpl1[1] + tpl2[1]
    d_diff = abs(tpl1[1] - tpl2[1])
    if center_distance == d_sum or center_distance == d_diff:
        return 1
    if d_diff < center_distance < d_sum:
        return 1
    else:
        # center1 is inside circle2
        if center_distance < tpl1[1] or center_distance < tpl2[1] :
            return 1

    return 0


def Solution(A):
    centersAndRadius = [(idx, item) for idx, item in enumerate(A)]

    intersections = 0
    for t1, t2 in combinations(centersAndRadius, 2):


        res = num_of_intersections(t1, t2)
        if res > 0:
            intersections += 1

        if intersections >=10000000.:
            return -1
    return intersections









