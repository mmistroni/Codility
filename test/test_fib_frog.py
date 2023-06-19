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

    def test_fibfrog2(self):
        A = []
        res = solution(A)
        self.assertEquals(1, res)

    def test_fibfrog3(self):
        A = [1]
        res = solution(A)
        self.assertEquals(1, res)


if __name__ == '__main__':
    unittest.main()
