import unittest
from count_nondivisble import solution, arrayF,  factorization

class MyTestCase(unittest.TestCase):

    def _find_factors(self, A):
        for item in range(1,20):
            F = arrayF(item)

            factors = set(factorization(item, F))
            print(f'{item}= {factors} ')


    def test_find_factors(self):
        A = [0] * 5
        A[0] = 3
        A[1] = 1
        A[2] = 2
        A[3] = 3
        A[4] = 6
        self._find_factors(A)


    def test_something(self):

        A = [0] * 5
        A[0] = 3
        A[1] = 1
        A[2] = 2
        A[3] = 3
        A[4] = 6
        expected = [2, 4, 3, 2, 0]

        result = solution(A)
        print(f'rsutl is {result}')

        self.assertEqual(expected, result)


if __name__ == '__main__':
    unittest.main()
