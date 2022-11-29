from itertools import permutations

def check(array_of_array, magic_sum):
    for i in range(0,3):
        # summing every row
        item = array_of_array[i]
        if sum(item) != magic_sum:
            return False
    # checking diagonal
    diagonal = [input[i][i] for i in range(0, 3)]
    if sum(diagonal) != magic_sum:
        return False

    arrays = [item]
    for i in range(0,3):
        pass



def solution(array_of_array):

    first = array_of_array[0:3]
    second = array_of_array[3:6]
    third = array_of_array[6:9]

    magic_sum = sum(first)






    return 0