#https://www.codewars.com/kata/65cf8417e2b49c2ecd3c3aee/train/python
'''
You are given a positive integer n.

The task is to calculate how many binary numbers without leading zeros (such that their length is n and they do not contain two zeros in a row) there are. Note that zero itself ("0") meets the conditions (for n = 1).

For example, there are three eligible binary numbers of length 3:

101
110
111
100 is not suitable.

Remember that n may be fairly big (up to 10^4). Good luck!


'''

import itertools

symbols = ['0', '1']

def _generate_combi(length_n):
    #combinations_tuples = list(itertools.product(symbols, repeat=length))
    # Join the elements of each tuple into a single string for cleaner output
    #return [''.join(combo) for combo in combinations_tuples]
    total_combinations = 2**length_n  # This is 8

    binary_list = []
    for i in range(total_combinations):
        # 1. Convert the integer 'i' to its binary string: bin(i)
        #    Example: i=1 -> '0b1', i=4 -> '0b100'
        # 2. Remove the '0b' prefix: [2:]
        # 3. Use zfill(length_n) to pad with leading zeros up to the required length (n)
        binary_string = bin(i)[2:].zfill(length_n)
        binary_list.append(binary_string)

    return binary_list

def zeros(n: int) -> int:
    
    combis = _generate_combi(n)
    if n == 1:
        return len(combis)
    filtered = [t for t in combis if '00' not in t and not t.startswith('0')]
    return len(filtered)