import unittest
from peaks import solution, find_peaks, divisors

class MyTestCase(unittest.TestCase):
    def test_something(self):
        A= [1, 2, 3, 4, 3, 4, 1, 2, 3, 4, 6, 2]
        self.assertEqual(3, solution(A))
        #from pprint import pprint
        #pprint(find_peaks(A))

    def test_something2(self):
        A= [1, 2, 3, 4, 3, 4, 1, 2, 3, 4, 6, 2]
        print(f'{divisors(len(A))}')



if __name__ == '__main__':
    unittest.main()
