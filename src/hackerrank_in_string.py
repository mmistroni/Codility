def trim(input, lst):
    if not lst:
        return 'YES'
    if not input:
        return 'NO'
    chr = input[0]
    if lst[0] == chr:
        return trim(input[1:], lst[1:])
    return trim(input[1:], lst)


def solution(input_string):
    holder = trim(input_string, 'hackerrank')

    return holder