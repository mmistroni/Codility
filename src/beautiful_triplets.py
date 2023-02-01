# https://www.hackerrank.com/challenges/beautiful-triplets/problem?isFullScreen=false&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen


def find_triplets(sequence, indexes, d):
    if not sequence:
        return indexes
    nxt = sequence.pop(0)
    latest = indexes[-1]
    if nxt - latest == d:
        indexes.append(nxt)
        return find_triplets(sequence, indexes, d)





def solution(sequence,d):
    counts = 0
    for idx in range(0, len(sequence)):
        # not working. we need to keep start, and give it to
        # a separate fun
        res = find_triplets(sequence, [idx], d)
        if len(res) == 3:
            counts +=1


    return counts