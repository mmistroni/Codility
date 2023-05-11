#https://app.codility.com/programmers/lessons/12-euclidean_algorithm/chocolates_by_numbers/
import logging
# https://www.researchgate.net/post/What-is-the-recurrence-relation-for-the-Euclidean-GCD-Algorithm
#https://www.hackerearth.com/practice/notes/euclid-algorithm-made-easy-1/#:~:text=There%20is%20a%20recurrence%20relation%20of%20the%20function,the%20base%20case%20is%20GCD%20%28a%2C0%29%20%3D%20a%3B

#https://www.researchgate.net/post/What-is-the-recurrence-relation-for-the-Euclidean-GCD-Algorithm

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