#https://app.codility.com/programmers/lessons/12-euclidean_algorithm/chocolates_by_numbers/
import logging

def solution(N, M):
    # Not good enough, this has to do with euclidean algorithm
    # hint. use binary bcd
    ## it's supposed to run in 0.1 seconds
    choc_array = [1] * N # we dont need to hold array. we just looop thru
                 # numbers and see if we have seen the current
    next = 0
    holder = []

    seen  = False

    while not seen:
        #logging.info(f'Eating {next}')
        if next not in holder:
            holder.append(next)
            next = (next + M) % N  # this is being done in euclidan algo
        else:
            seen = True

    return len(holder)