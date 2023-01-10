#https://www.hackerrank.com/challenges/climbing-the-leaderboard/problem?h_r=next-challenge&h_v=zen

from heapq import heappush, heapify, nlargest, nsmallest


def solution(ranked, player):
    holder = []
    for item in player:
        tst = [i * -1 for i in set(ranked)]
        new_item  = item * -1
        tst.append(new_item)
        tst  = list(tst)
        heapify(tst)
        elems = nsmallest(len(tst), tst)
        idx = elems.index(new_item) + 1 % 6
        holder.append(idx)

    return holder