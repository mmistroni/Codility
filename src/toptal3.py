'''
An industrial company ha sN factories,, each producing some pollution and has decided
to reduce is total fumes bny equipping some of htem with filters
Every suchfilter reduces the pollution of a factory by half.
When a second filter is applied it  again reduces by half hte remaining pollution
For example, a factory that produces 6 unit of pollution will generate 1.5 units with 2 filters
and 0.75 with three
You are given a function, which  given an array of N integers dsecribing the amount of pollution
Your task is to find the minimun numbners of iltgers needed to reduce pollution by half
Below are the usecsaes
'''

from itertools import product
import heapq
def calculate_emission(input_array):
    '''
    Calculate emissions
    :param tuple emission_vs_filter_tpl: a tuple of ([factory_emissions], [filter combinations]
    :return int: the reduced emissions after applying filters
    '''
    minimized_list = [item * -1 for item in input_array if item !=0]

    target_sum = sum(minimized_list) / 2

    max_filters = len(minimized_list)

    heapq.heapify(minimized_list)

    start_sum = target_sum -1

    filters = 0

    while start_sum < target_sum:
        smallest = heapq.heappop(minimized_list)
        smallest *= 0.5
        filters += 1
        heapq.heappush(minimized_list, smallest)
        start_sum = sum(minimized_list)


    return min(filters, max_filters)


def install_filters(A):
    return calculate_emission(A)


def solution(A):
    return install_filters(A)

