import unittest
from flags import solution


class MyTestCase(unittest.TestCase):

    def check(self, peaks, flags):
        pass

    def evaluate(self, peaks):
        '''
        Flags can only be set on peaks.
        What's more, if you take K flags,
        then the distance between any two flags should be greater than or equal to K.
        The distance between indices P and Q is the absolute value
        '''
        fill_array = [0] * max(peaks) + 1
        for p in peaks:
            fill_array[p] = 1
        from pprint import pprint
        pprint(fill_array)

        # Possible solution we need to loop , add flags
        # and check , at every step, if we have a flag at idx+4



    def test_something(self):

        A = [None]* 12
        A[0] = 1
        A[1] = 5
        A[2] = 3
        A[3] = 4
        A[4] = 3
        A[5] = 4
        A[6] = 1
        A[7] = 2
        A[8] = 3
        A[9] = 4
        A[10] = 6
        A[11] = 2

        peaks = solution(A)
        print(peaks)
        self.assertEqual(3, solution(A))


if __name__ == '__main__':
    unittest.main()
