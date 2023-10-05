import unittest

from minmaxdivision import solution

class MyTestCase(unittest.TestCase):

    def test_something(self):
        # Not good. we need to generalize where we can split the array
        # in n parts
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
