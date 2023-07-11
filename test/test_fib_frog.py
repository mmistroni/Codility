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


    def probe(self, prev, next, d):
        diff = next - prev
        if diff in d.keys():
            return True
        return False

    def test_fibfrog(self):
        A = [0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0]
        res = solution(A)
        self.assertEquals(3, res)

    def test_combination(self):
        A = [0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0]


        ones = [idx for idx in range(0, len(A)) if A[idx] == 1]
        ones = [-1] + ones + [len(A)]

        # we need to build adjacency list so that then we can
        # find the shortest path
        # or mayb try another approach. once you start, find all
        # the possible next paths from start
        # -1 3
        # -1 4
        # -1 6
        # -1 11
        # then remove the ones that are not fibonacci
        # get last index.and repeat same process
        #
        

    def test_fibfrog2(self):
        A = []
        res = solution(A)
        self.assertEquals(1, res)

    def test_fibfrog3(self):
        A = [1]
        res = solution(A)
        self.assertEquals(1, res)

    def test_fibfrog4(self):
        A = [1, 1, 1]
        res = solution(A)
        self.assertEquals(2, res)

    def test_zeros(self):
        A = [0, 0, 0]
        res = solution(A)
        self.assertEquals(-1, res)

    def test_anotherfail(self):
        A =  [0, 0, 0, 1, 0]
        res = solution(A)
        self.assertEquals(-1, res)


if __name__ == '__main__':
    unittest.main()
