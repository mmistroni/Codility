import unittest

from src.triangular_triplets import solution
class MyTestCase(unittest.TestCase):
    def test_something(self):
        A = [ 10, 2, 5, 1, 8,20]
        self.assertEqual(1, solution(A))

    def checker(self, p, q, r):
        return (p + q) > r and \
               (q + r) > p and \
               (r + p) > q

    def result(self, A):
        s_a = sorted(A, key=lambda x: x)
        for i in range(0, len(A) - 3):
            p = s_a[i]
            q = s_a[i + 1]
            r = s_a[i + 2]
            if self.checker(p, q, r):
                return 1
        return 0

    def test_empty(self):
        # expeted sol = Triplet (0, 2, 4) is triangular. 10 5 8
        A = [5, 3, 3]
        self.assertEqual(1, solution(A))



if __name__ == '__main__':
    unittest.main()
