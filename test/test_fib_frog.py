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
        if diff in d:
            return True
        return False



    def test_fibfrog(self):
        A = [0, 0, 0, 1, 1, 0, 1, 0, 0, 0]

        seq = fibonacci_seq(len(A))[0:len(A)]

        d = dict((seq[i], i) for i in range(0, len(seq)))

        if len(A) in d:
            return 1

        ones = [idx for idx in range(0, len(A)) if A[idx] == 1]

        ones.append(len(A))

        # Find the last step and gon
        diff_to_start = [idx - (-1)  for idx in ones]

        exists = [(idx, idx in d.keys()) for idx in diff_to_start ]

        # Filter to find the trues one
        # then loop agian to find differences from current idx. We assume there is only one soution

        #we jump to the first and hten we recalculate next fib

        # We need two separate loop.
        print('Out')

if __name__ == '__main__':
    unittest.main()
