import re
from collections import defaultdict


def test_score(test_str):
    if test_str == "OK":
        return True
    return False



def build_keys(testname, rest):
    trimmed = rest.replace(testname, '')
    number_pattern = re.compile(r'[\d]+')
    test_no = number_pattern.findall(trimmed)[0]
    return (testname, test_no)

def _map_to_test_keys(T):
    pattern = re.compile(r'[a-zA-Z]+')
    first_item = T[0]
    testname = pattern.findall(first_item)[0]
    tuple_keys = map(lambda test: build_keys(testname, test), T)
    return tuple_keys


def solution(T, R):
    # write your code in Python 3.8.10

    keys = _map_to_test_keys(T)
    zipped = list(zip(keys, R))

    holder = defaultdict(list)
    for testname, testresult in zipped:
        holder[testname].append(test_score(testresult))

    successes  =0
    for testname, results in holder.items():
        if all(results):
            successes +=1

    return (successes * 100) // len(holder)
