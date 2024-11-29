import unittest

from src.hamming_numbers import hamming
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

    def nth_hamming_number(self, n):
        """
        Finds the nth Humming number.
        """
        left, right = 1, float('inf')
        while left < right:
            mid = (left + right) // 2
            exp2, exp3, exp5 = 0, 0, 0
            while 2 ** exp2 * 3 ** exp3 * 5 ** exp5 < mid:
                exp2 += 1
                if 2 ** exp2 * 3 ** exp3 * 5 ** exp5 >= mid:
                    break
            while 3 ** exp3 * 5 ** exp5 < mid:
                exp3 += 1
                if 2 ** exp2 * 3 ** exp3 * 5 ** exp5 >= mid:
                    break
            while 5 ** exp5 < mid:
                exp5 += 1
                if 2 ** exp2 * 3 ** exp3 * 5 ** exp5 >= mid:
                    break
            if 2 ** exp2 * 3 ** exp3 * 5 ** exp5 < n:
                left = mid + 1
            else:
                right = mid
        return 2 ** exp2 * 3 ** exp3 * 5 ** exp5


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

    def test_bignumner(self):
        
        res = self.nth_hamming_number(10005000)

        #print(f'last item is:{res}')

        #self.assertEqual(res, 1660753125)

        #self.assertEqual(self.generate_itertools(1638), 1660753125, "hamming(1638) should be 1660753125)")
        #self.assertEqual(self.generate_itertools(1794), 3375000000, "hamming(1794) should be 3375000000)")

    from heapq import heappush, heappop

    def get_nth_hamming_number(self, n):
        """
        This function finds the nth Hamming number using the modified Fibonacci approach.
        Args:
            n: The index of the desired Hamming number.
        Returns:
            The nth Hamming number.
        """
        h = [1]
        p2, p3, p5 = 0, 0, 0
        for _ in range(n - 1):
            next_num = min(2 * h[p2], 3 * h[p3], 5 * h[p5])
            h.append(next_num)
            if next_num % 2 == 0:
                p2 += 1
            if next_num % 3 == 0:
                p3 += 1
            if next_num % 5 == 0:
                p5 += 1
        return h[-1]
    # Example usage

    def test_new_algo(self):
        self.assertEqual(self.get_nth_hamming_number(1), 1, "hamming(1) should be 1")  # 2 ^ 0 * 3^0 * 5^0
        self.assertEqual(self.get_nth_hamming_number(2), 2, "hamming(2) should be 2")  # 2 ^ 1
        self.assertEqual(self.get_nth_hamming_number(3), 3, "hamming(3) should be 3")  # 3 ^ 1
        self.assertEqual(self.get_nth_hamming_number(4), 4, "hamming(4) should be 4")  # 2 ^ 2
        self.assertEqual(self.get_nth_hamming_number(5), 5, "hamming(5) should be 5")
        self.assertEqual(self.get_nth_hamming_number(6), 6, "hamming(6) should be 6")
        self.assertEqual(self.get_nth_hamming_number(7), 8, "hamming(7) should be 8")
        self.assertEqual(self.get_nth_hamming_number(8), 9, "hamming(8) should be 9")
        self.assertEqual(self.get_nth_hamming_number(9), 10, "hamming(9) should be 10")
        self.assertEqual(self.get_nth_hamming_number(10), 12, "hamming(10) should be 12")
        self.assertEqual(self.get_nth_hamming_number(11), 15, "hamming(11) should be 15")
        self.assertEqual(self.get_nth_hamming_number(12), 16, "hamming(12) should be 16")
        self.assertEqual(self.get_nth_hamming_number(13), 18, "hamming(13) should be 18")
        self.assertEqual(self.get_nth_hamming_number(14), 20, "hamming(14) should be 20")
        self.assertEqual(self.get_nth_hamming_number(15), 24, "hamming(15) should be 24")
        self.assertEqual(self.get_nth_hamming_number(16), 25, "hamming(16) should be 25")
        self.assertEqual(self.get_nth_hamming_number(17), 27, "hamming(17) should be 27")
        self.assertEqual(self.get_nth_hamming_number(18), 30, "hamming(18) should be 30")
        self.assertEqual(self.get_nth_hamming_number(19), 32, "hamming(19) should be 32")
        #self.assertEqual(self.nth_hamming_number(1638), 1660753125, "hamming(19) should be 32")
        #self.assertEqual(self.nth_hamming_number(1794), 3375000000, "hamming(19) should be 32")


if __name__ == '__main__':
    unittest.main()
