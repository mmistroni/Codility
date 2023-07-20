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


    def probe(self, A):
        seq = fibonacci_seq(max(len(A), 10))[1:]
        fib_dict = dict((seq[i], i) for i in range(0, len(seq)))

        ones = [idx for idx in range(0, len(A)) if A[idx] == 1]
        ones = [-1] + ones + [len(A)]

        counter = 0
        current = ones[0]
        for i in ones[1:]:
            c_idx = ones.index(current)
            nextes = find_next(current, ones[c_idx + 1:], fib_dict)
            if nextes:
                counter += 1
                current = nextes[-1]

        print(f'At the end of loop we got:{counter}')
        return counter if counter > 0 else -1

    def find_all_trees(self, A):
        def find_all_next(start_idx, remainder, fib_dict):
            return [i for i in remainder if (i - start_idx) in fib_dict.keys()]

        seq = fibonacci_seq(max(len(A), 10))[1:]
        fib_dict = dict((seq[i], i) for i in range(0, len(seq)))
        ones = [idx for idx in range(0, len(A)) if A[idx] == 1]

        adj_list_dict = {}
        ones = [-1] + ones + [len(A)]
        for idx, item in enumerate(ones):
            nxts  = find_all_next(item, ones[idx+1:], fib_dict)
            adj_list_dict[item] = nxts
        adj_list_dict[ones[-1]] = ones[-1]
        return adj_list_dict


    def test_newtest(self):
        # Not quite there. we need to check the indexes that got he
        A = [1, 1, 0, 0, 0]
        res = self.find_all_trees(A)
        for k, v in res.items():
            print(f'Idx:{k}. Next:{v}')
        print('---- NEXT --')
        A = [0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0]
        res = self.find_all_trees(A)
        for k, v in res.items():
            print(f'Idx:{k}. Next:{v}')

    def test_fibfrog(self):

        res = solution(A)
        self.assertEquals(3, res)

    def test_combination(self):
        A = [0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0]
        res = self.probe(A)
        self.assertEquals(3, res)


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

    def test_anotheranotherfail(self):
        A = [1, 1, 0, 0, 0]
        res = solution(A)
        self.assertEquals(2, res)


if __name__ == '__main__':
    unittest.main()
