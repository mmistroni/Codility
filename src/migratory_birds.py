from collections import Counter

def solution(input_array):
    result = Counter(input_array).items()
    sorted_res = sorted(result, key=lambda tpl: (tpl[1], -tpl[0]), reverse=True)
    return sorted_res[0][0]
