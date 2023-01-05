#https://www.hackerrank.com/challenges/climbing-the-leaderboard/problem?h_r=next-challenge&h_v=zen

from heapq import heappush, heapify, nlargest


def solution(ranked, player):
    holder = []
    for item in player:
        tst = [i * -1 for i in set(ranked)]
        heapify(tst)
        new_item = item * -1
        heappush(tst, new_item)
        idx = tst.index(new_item) + 1
        holder.append(idx)

    return holder