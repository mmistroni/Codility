import unittest

from src.count_div import solution
from src.prefix_sums import generate_prefix_sum, prefix_sums

class MyTestCase(unittest.TestCase):
    def test_something(self):
        A = 6
        B = 11
        K = 2
        self.assertEqual(3, solution(A, B, K))

    def test_prefixsums(self):
        A = list(range(1,11))
        print(f'A IS:\n{A}')
        print(generate_prefix_sum(A))
        print('=------')
        print(prefix_sums(A))




if __name__ == '__main__':
    unittest.main()
