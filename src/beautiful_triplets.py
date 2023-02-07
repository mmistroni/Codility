# https://www.hackerrank.com/challenges/beautiful-triplets/problem?isFullScreen=false&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen


def find_triplets(sequence, indexes, d):
    #
    while sequence:
        if len(indexes) == 3:
            break
        latest = indexes[-1]
        try:
            fellow = latest + d
            next = sequence.index(fellow)
            indexes.append(fellow)
        except Exception as e:
            break

    return indexes

def solution(sequence,d):
    counts = 0
    for idx in range(0, len(sequence)):
        # not working. we need to keep start, and give it to
        # a separate fun
        res = find_triplets(sequence[idx+1:], [sequence[idx]], d)
        if len(res) == 3:
            counts +=1
        continue

    return counts