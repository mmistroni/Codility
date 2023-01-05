#https://www.hackerrank.com/challenges/climbing-the-leaderboard/problem?h_r=next-challenge&h_v=zen

from heapq import heappush, heapify, nlargest


def solution(ranked, player):
    tst =  [i * -1 for i in set(ranked)]
    holder = []
    for item in player:
        new_item = item *-1
        tst.append(new_item)
        heapify(tst)
        idx = tst.index(new_item) + 1
        holder.append(idx)
        tst.remove(new_item)
    return holder