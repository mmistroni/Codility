import unittest
from flags import solution


class MyTestCase(unittest.TestCase):



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
        self.assertEqual(3, peaks)

if __name__ == '__main__':
    unittest.main()
