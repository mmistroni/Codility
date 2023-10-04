import unittest

from minmaxdivision import solution

class MyTestCase(unittest.TestCase):

    def test_something(self):
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
            mid = (beg + end) // K
            mid2 = (mid  + end) // 2

            first = A[beg:mid]
            second = A[mid:mid2]
            third = A[mid2:end]
            holders.append([first, second , third] )
            beg = mid + 1
            end = end -1

        from pprint import pprint
        pprint(holders)
        self.assertEqual(True, True)


if __name__ == '__main__':
    unittest.main()
