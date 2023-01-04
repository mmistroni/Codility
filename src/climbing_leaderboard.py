#https://www.hackerrank.com/challenges/climbing-the-leaderboard/problem?h_r=next-challenge&h_v=zen

from heapq import heappush, heapify, nlargest


def repackage_list(input):
    ranked = [i * -1 for i in input]

    heapify(ranked)

    return ranked

def solution(ranked, player):
    tst =repackage_list(ranked)
    holder = []
    for item in player:
        new_item = item *-1
        heappush(tst, new_item)
        holder.append(tst.index(new_item) + 1)
    return holder