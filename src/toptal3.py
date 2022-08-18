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

def calculate_emission(emission_vs_filter_tpl):
    '''
    Calculate emissions
    :param tuple emission_vs_filter_tpl: a tuple of ([factory_emissions], [filter combinations]
    :return int: the reduced emissions after applying filters
    '''
    reduced_emissions = [tpl[0] * (.5 ** tpl[1]) for tpl in
                         emission_vs_filter_tpl]
    return sum(reduced_emissions)


def install_filters(A):
    # removing zeros, they don tcount
    no_zeros = [n for n in A if n > 0]

    # All possible combination of filters we can install, from 0
    # until 1 * len(no_zeors)
    # We have an upper bound which is installing 1 filter per factory to
    # to reduce emissions by half.
    # This is what we are trying to beat
    res = list(product(range(0, len(no_zeros)+1), repeat=len(A)))

    filtered = [tpl for tpl in res if sum(tpl) <= len(A)] # No point having more filters than minimum(1 x len(A))
    result = []
    for idx, tpl in enumerate(filtered):
        emission_vs_filter_tuple = list(zip(no_zeros, tpl)) # zipping emissions and filter_combination
        result.append((tpl, calculate_emission(emission_vs_filter_tuple)))

    good_ones = [tpl for tpl in result if tpl[1] <= sum(A)/ 2]
    sorted_tpls = sorted(good_ones, key=lambda t: sum(t[0]))
    return sum([i for i in sorted_tpls[0][0]])

def solution(A):
    return install_filters(A)

