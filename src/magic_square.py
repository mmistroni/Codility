from itertools import permutations

#https://medium.com/enjoy-algorithm/how-to-solve-magic-square-puzzle-7ced6ee5dd
#https://www.hackerrank.com/challenges/magic-square-forming/problem
import numpy as np

def _find_pairs_up_to_10(input, seen):
    pass


def check(input, magic_sum):
    a = np.array(input)

    magic_sum = sum(input[0])
    print(f'Checkign for sum euqal to {magic_sum}')
    for i in range(0, 3):
        col = a[:, i]
        row = a[i, :]
        if not sum(col) == magic_sum:
            return False
        if not sum(row) == magic_sum:
            return False
    return True

def build_magixbox():
    items = list(range(1,10))
    first = [0] * 3
    second = [0] * 3
    third = [0] * 3

    items.remove(5)
    second[1] = 5



def solution(array_of_array):

    magixboxes = [
        [[2, 9, 4], [7, 5, 3],[6, 1, 8]],
        [[6, 7, 2], [1, 5, 9], [8, 3, 4]],
        [[8, 1, 6], [3, 5, 7], [4, 9, 2]],
        [[4, 3, 8], [9, 5, 1], [2, 7, 6]],
        [[4, 9, 2], [3, 5, 7], [8, 1, 6]],
        [[8, 3, 4], [1, 5, 9], [6, 7, 2]],
        [[6, 1, 8], [7, 5, 3], [2, 9, 4]],
        [[2, 7, 6], [9, 5, 1], [4, 3, 8]]]



    


    first, second, third = array_of_array

    magic_sum = 15

    # place 5 in central cell
    # then remove 5 and find pairs up to 10
    # place it 'somewhere' and see if you can sum up 10
    # carry on doing it


    holder = []
    for one in permutations(first, 3):
        for two in permutations(second, 3):
            for three in permutations(third, 3):
                arr = [one, two, three]
                if check(arr, magic_sum):
                    holder.append(sum(one))

    return sum(holder)





    return 0