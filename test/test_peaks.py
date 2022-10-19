import unittest
from peaks import solution, find_peaks, divisors

class MyTestCase(unittest.TestCase):
    def test_something(self):
        A= [1, 2, 3, 4, 3, 4, 1, 2, 3, 4, 6, 2]
        #self.assertEqual(3, solution(A))
        from pprint import pprint
        pprint(find_peaks(A))

    def test_something(self):
        A= [1, 2, 3, 4, 3, 4, 1, 2, 3, 4, 6, 2]
        res = list(map(lambda d: len(A) // d, divisors(len(A))))

        print(f'Sblists{res}')

        from itertools import islice

        # Not good enough we need to split properly in code below
        # then we need to check how many peaks are in each items
        alls = [list(islice(iter(A), elem))
                for elem in res]
        from pprint import pprint
        pprint(alls)

        print(f'We have following divisors:{res}')


if __name__ == '__main__':
    unittest.main()
