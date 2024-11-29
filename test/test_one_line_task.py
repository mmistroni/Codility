import unittest
from src.one_line_task import solution, factorial
from itertools import combinations

def combi(n, k):
    return  combinations(range(1,n), k)


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(120, factorial(5))

    def test_combis(self):
        tests  =[ (6, 3, 20),
          (6, 4, 15),
          (6, 9, 0)
        ]

        for n, k, res in tests:
            self.assertEqual(res, combi(n, k))

    def test_combi(self):
        self.assertEquals(560, solution(16, 3))



if __name__ == '__main__':
    unittest.main()
