from itertools import permutations

#https://medium.com/enjoy-algorithm/how-to-solve-magic-square-puzzle-7ced6ee5dd
#https://www.hackerrank.com/challenges/magic-square-forming/problem

import numpy as np

def solution(array_of_array):

    # Not good we need to sort it out without numpy
    magixboxes = [
        [[2, 9, 4], [7, 5, 3],[6, 1, 8]],
        [[6, 7, 2], [1, 5, 9], [8, 3, 4]],
        [[8, 1, 6], [3, 5, 7], [4, 9, 2]],
        [[4, 3, 8], [9, 5, 1], [2, 7, 6]],
        [[4, 9, 2], [3, 5, 7], [8, 1, 6]],
        [[8, 3, 4], [1, 5, 9], [6, 7, 2]],
        [[6, 1, 8], [7, 5, 3], [2, 9, 4]],
        [[2, 7, 6], [9, 5, 1], [4, 3, 8]]]

    tmp = array_of_array
    holder = []
    for item in magixboxes:
        diffs = []
        for i in range(0, 3):
            for j in range(0, 3):
                mx = tmp[i][j]
                oth = item[i][j]
                diffs.append(abs(mx - oth))
        holder.append(sum(diffs))

    return min(holder)


