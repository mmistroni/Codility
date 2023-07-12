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

def find_next(start, nextes, fib_dict):
    holder = []
    for i in nextes:
        diff = i - start
        if diff in fib_dict.keys():
            holder.append(i)

    return holder


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
        seq = fibonacci_seq(max(len(A), 10))[1:]
        fib_dict = dict((seq[i], i) for i in range(0, len(seq)))

        ones = [idx for idx in range(0, len(A)) if A[idx] == 1]
        ones = [-1] + ones + [len(A)]

        holders = []
        counter = 0
        current = ones[0]
        for i in ones[1:]:
            c_idx = ones.index(current)
            nextes = find_next(current, ones[c_idx + 1:], fib_dict)
            if nextes:
                counter +=1
                current = nextes[-1]



        print(f'At the end of loop we got:{counter}')

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
