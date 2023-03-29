import unittest
from count_nondivisble import solution

class MyTestCase(unittest.TestCase):
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
