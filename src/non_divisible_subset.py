##https://www.hackerrank.com/challenges/non-divisible-subset/problem?isFullScreen=true
from itertools import combinations, chain
from collections import Counter
def solution(arr, k):
    remainders = [i%k for i in arr]


    counts = Counter(remainders)

    # we dont loop

    holder = []

    # we check case 0
    holder.append(min(counts.get(0,0), 1))

    # case k/2
    if k % 2 == 0:
        holder.append(min(counts.get(k // 2, 0), 1))
    # then loop from 1 to k-1 and check
    for p in range(1, k//2 + 1):

        if p != k - p:

            holder.append(max(counts.get(p), counts.get(q)))
    

    return sum(holder)



'''
     #https://medium.com/@mrunankmistry52/non-divisible-subset-problem-comprehensive-explanation-c878a752f057
     Here's my take on this problem. I deconstructed all the numbers into num%k because we don't really care about the whole number
      - just it's remainder. 
      for each i in <1, k-1> (that is results of modulo) we have exclusive unique unordered pairs (i, k-i) 
      (eg. k=5 : (1, 4), (2, 3) that would sum to k if added, 
      therefore we add to the count only the max number of occurences from the pair counts. 
      We can also always add only one 0 and if k%2==0 one k/2 number.
    '''



