import unittest

from fib_frog import solution


def fibonacci_seq(n):
    fib = [0] * (n+2)
    fib[1] = 1
    for i in range(2, n+1):
        fib[i] = fib[i-1] + fib[i-2]
    return fib

def fibonacci2(n):
    if n == 0:
        return 0
    fib = [0] * (n+1)
    fib[1] = 1
    for i in range(2, n+1):
        fib[i] = fib[i-1] + fib[i-2]
    return fib[n]

class MyTestCase(unittest.TestCase):
    def test_fibfrog(self):
        A = [0] * 11
        A[0] = 0
        A[1] = 0
        A[2] = 0
        A[3] = 1
        A[4] = 1
        A[5] = 0
        A[6] = 1
        A[7] = 0
        A[8] = 0
        A[9] = 0
        A[10] = 0

        seq = fibonacci_seq(len(A))[0:len(A)]

        d = dict((seq[i], i) for i in range(0, len(seq)))


        ones = [idx for idx in range(0, len(A)) if A[idx] == 1]
        ones.append(len(A))
        print(f'Fib Seq :{seq}|ones:{ones}')
        print(f'Dict:{d}')

        # Need to find distances between ones and find out which of these
        # distances are fibonacci numbers


        res = solution(A)
        self.assertEqual(3,  res)


if __name__ == '__main__':
    unittest.main()
