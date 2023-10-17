import unittest

from minmaxdivision import solution


def binarySearch(A, x):
    n = len(A)
    beg = 0
    end = n - 1
    result = -1
    holders = []
    while beg <= end: # Nearly there.
        mid = (beg + end) // 2
        print(f'beg:{beg}|mid:{mid}')
        # this sort of work but we need to find out how the
        # binary seach work. and we need to keep track of beginning and mid so that
        # we can vary the array
        if A[mid] <= x:
            holders.append((beg, end, mid, A[beg:mid], A[mid:end]))
            beg = mid + 1
            print(f'mid:{mid}, {A[mid]} vs {x}')
            result = mid
        else:
            end = mid -1
    return result, holders

def binarySplit(A):
    n = len(A)
    beg = 0
    end = n - 1
    mid = (beg + end) // 2

    return A[beg:mid], A[mid:]

class MyTestCase(unittest.TestCase):

    def test_binsplit(self):
        # New idea
        '''
            We start with whole array plus two dummies
            then we split the first and get rid of a dummy -  we need a datastructure for that, perhaps a
            circular buffer
            then we advance start of one
        '''

        :return:
        '''
        A = [1, 5, 1, 2, 2, 2]
        M = 5
        K = 3
        res = binarySplit(A, 3)
        startSum = sum(sum(A))
        # split in two
        start_idx = 0
        end_idx = len(A)-1

        # For now  we ignore M

        sequences =[]
        sequences.append(A)
        for i in range(1, K):
            sequences.append([])
        pprint(sequences)



    def test_binsearch(self):
        A = [1, 5, 1, 2, 2, 2]
        K = 3
        M = 5

        sortd_a = sorted(A, key = lambda x:x)

        out, holders = binarySearch(sortd_a, M )


        print(f'out is:{out}')
        from pprint import pprint
        pprint(holders)

        # we dont have as roted array so binary searchis an ago that should be used
        # to recursivey split the lists


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
