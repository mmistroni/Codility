import unittest

from minmaxdivision import solution


def binarySearch(A, x):
    n = len(A)
    beg = 0
    end = n - 1
    result = -1
    while beg <= end:
        mid = (beg + end) // 2
        print(f'beg:{beg}|mid:{mid}')
        if A[mid] <= x:
            beg = mid + 1
            print(f'mid:{mid}, {A[mid]} vs {x}')
            result = mid
        else:
            end = mid -1
    return result

def chunkIt(seq, num):
    avg = len(seq) / float(num)
    out = []
    last = 0.0

    while last < len(seq):
        out.append(seq[int(last):int(last + avg)])
        last += avg

    return out


class MyTestCase(unittest.TestCase):


    def test_binsearch(self):
        A = [1, 5, 1, 2, 2, 2]
        K = 3
        M = 5
        print(binarySearch(A, M ))
        # we dont have as roted array so binary searchis an ago that should be used
        # to recursivey split the lists


    def test_checksplits(self):
        A = [1, 5, 1, 2, 2, 2]
        K = 3

        chunks = chunkIt(A, K)

        maxSize = len(A) // K
        print(f'A={A}')
        for i in range(0, K):
            s = i * maxSize
            e = min(s + maxSize, len(A))
            arr = A[s:e]
            print(f'{i} = {arr}')

    def test_something(self):
        # Idea
        # we split the array in N pieces and run
        # same as binary search on each piece



        K = 3
        M = 5
        A = [1,5, 1, 2, 2, 2]

        n = len(A)
        beg = 0
        end = n-1
        holders = []

        # Idea is right, but not quite there yet.we need to split the array in slices
        # where we vary the length of each array

        while beg <= end:
            mid = (beg + end) // 2
            if beg == 0:
                first = A[beg:mid]
                second = A[mid:]
                third = []
            else:
                first = A[0:beg]
                second = A[beg:mid]
                third = A[mid:]
            holders.append(max(sum(first), sum(second) , sum(third) ))
            beg += 1


        from pprint import pprint
        pprint(holders)

        sorted_holders = sorted(holders, key=lambda x:x)

        self.assertEquals(6, sorted_holders[0])




if __name__ == '__main__':
    unittest.main()
