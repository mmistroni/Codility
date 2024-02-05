import unittest

from hamming_numbers import hamming
from heapq import heapify, heappop, heapreplace, heappush


# https://en.wikipedia.org/wiki/Regular_number#:~:text=In%20computer%20science%2C%20regular%20numbers%20are%20often%20called,used%20as%20a%20test%20case%20for%20functional%20programming.
from heapq import heapify, heappop, heapreplace


def comput_hamming(n):
    #create 3 iterables and merge them together
    # https://stackoverflow.com/questions/5023266/merge-join-two-generators-in-python


   # H = 2**i * 3**j * 5 **k
    pass

class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(hamming(1), 1, "hamming(1) should be 1") #2 ^ 0 * 3^0 * 5^0
        self.assertEqual(hamming(2), 2, "hamming(2) should be 2") #2 ^ 1
        self.assertEqual(hamming(3), 3, "hamming(3) should be 3") #        3 ^ 1
        self.assertEqual(hamming(4), 4, "hamming(4) should be 4") #2 ^ 2
        self.assertEqual(hamming(5), 5, "hamming(5) should be 5")
        self.assertEqual(hamming(6), 6, "hamming(6) should be 6")
        self.assertEqual(hamming(7), 8, "hamming(7) should be 8")
        self.assertEqual(hamming(8), 9, "hamming(8) should be 9")
        self.assertEqual(hamming(9), 10, "hamming(9) should be 10")
        self.assertEqual(hamming(10), 12, "hamming(10) should be 12")
        self.assertEqual(hamming(11), 15, "hamming(11) should be 15")
        self.assertEqual(hamming(12), 16, "hamming(12) should be 16")
        self.assertEqual(hamming(13), 18, "hamming(13) should be 18")
        self.assertEqual(hamming(14), 20, "hamming(14) should be 20")
        self.assertEqual(hamming(15), 24, "hamming(15) should be 24")
        self.assertEqual(hamming(16), 25, "hamming(16) should be 25")
        self.assertEqual(hamming(17), 27, "hamming(17) should be 27")
        self.assertEqual(hamming(18), 30, "hamming(18) should be 30")
        self.assertEqual(hamming(19), 32, "hamming(19) should be 32")

    def all_even(self):
        n = 0
        while True:
            yield n
            n += 2

    def PowTwoGen(self, max=0):
        n = 0
        while n < max:
            yield 2 ** n
            n += 1

    def mergeIT(self, *iterables):
        from heapq import heapify, heappop, heapreplace
        '''Merge multiple sorted inputs into a single sorted output.

        Similar to sorted(itertools.chain(*iterables)) but returns a generator,
        does not pull the data into memory all at once, and assumes that each of
        the input streams is already sorted (smallest to largest).

        >>> list(merge([1,3,5,7], [0,2,4,8], [5,10,15,20], [], [25]))
        [0, 1, 2, 3, 4, 5, 5, 7, 8, 10, 15, 20, 25]

        '''
        _heappop, _heapreplace, _StopIteration = heappop, heapreplace, StopIteration
        print('------- mergeIT')
        h = []
        h_append = h.append
        for itnum, it in enumerate(map(iter, iterables)):
            try:
                next = it.next
                h_append([next(), itnum, next])
            except _StopIteration:
                pass
        heapify(h)

        while 1:
            try:
                while 1:
                    v, itnum, next = s = h[0]  # raises IndexError when h is empty
                    yield v
                    s[0] = next()  # raises StopIteration when exhausted
                    _heapreplace(h, s)  # restore heap condition
            except _StopIteration:
                _heappop(h)  # remove empty iterator
            except IndexError:
                return
    def generate_itertools(self, n):
        return hamming(n)
        x = []
        setter = set()
        setter.add(1)
        heapify(x)
        heappush(x, 1)
        cur = 0
        for i in range(1 ,n+1):
            cur = heappop(x) # We dont remove..we need to keep so we can get item
            heappush(x, cur * 2)
            heappush(x, cur * 3)
            heappush(x, cur * 5)
            setter.add(cur * 2)
            setter.add(cur * 3)
            setter.add(cur * 5)

        return list(setter)

    def test_anotherit(self):
        #first_10_n = 10

        #res = self.generate_itertools(first_10_n)
        self.assertEqual(self.generate_itertools(1), 1, "hamming(1) should be 1")  # 2 ^ 0 * 3^0 * 5^0
        self.assertEqual(self.generate_itertools(2), 2, "hamming(2) should be 2")  # 2 ^ 1
        self.assertEqual(self.generate_itertools(3), 3, "hamming(3) should be 3")  # 3 ^ 1
        self.assertEqual(self.generate_itertools(4), 4, "hamming(4) should be 4")  # 2 ^ 2
        self.assertEqual(self.generate_itertools(5), 5, "hamming(5) should be 5")
        self.assertEqual(self.generate_itertools(6), 6, "hamming(6) should be 6")
        self.assertEqual(self.generate_itertools(7), 8, "hamming(7) should be 8")
        self.assertEqual(self.generate_itertools(8), 9, "hamming(8) should be 9")
        self.assertEqual(self.generate_itertools(9), 10, "hamming(9) should be 10")
        self.assertEqual(self.generate_itertools(10), 12, "hamming(10) should be 12")
        self.assertEqual(self.generate_itertools(11), 15, "hamming(11) should be 15")
        self.assertEqual(self.generate_itertools(12), 16, "hamming(12) should be 16")
        self.assertEqual(self.generate_itertools(13), 18, "hamming(13) should be 18")
        self.assertEqual(self.generate_itertools(14), 20, "hamming(14) should be 20")
        self.assertEqual(self.generate_itertools(15), 24, "hamming(15) should be 24")
        self.assertEqual(self.generate_itertools(16), 25, "hamming(16) should be 25")
        self.assertEqual(self.generate_itertools(17), 27, "hamming(17) should be 27")
        self.assertEqual(self.generate_itertools(18), 30, "hamming(18) should be 30")
        self.assertEqual(self.generate_itertools(19), 32, "hamming(19) should be 32")

        #for idx, x in enumerate(res):
        #    print(f'({idx+1}) = {x}')





if __name__ == '__main__':
    unittest.main()
