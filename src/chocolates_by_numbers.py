#https://app.codility.com/programmers/lessons/12-euclidean_algorithm/chocolates_by_numbers/
import logging

def solution(N, M):
    choc_array = [1] * N
    next = 0
    holder = []
    while(choc_array[next] != 0):
        #logging.info(f'Eating {next}')
        choc_array[next] = 0
        holder.append(next)
        next = (next + M) % N

    return len(holder)