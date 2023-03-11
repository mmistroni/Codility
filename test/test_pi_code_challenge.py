import unittest

from pi_code_challenge import solution
class MyTestCase(unittest.TestCase):
    def test_something(self):
        p, q  = "abc", 'bcd'

        self.assertEqual(2, solution(p, q))

    def test_something2(self):
        p, q  = "axxz", 'yzwy'

        self.assertEqual(2, solution(p, q))

    def test_something3(self):
        p, q  = "bacad", 'abada'

        self.assertEqual(1, solution(p, q))

    def test_something4(self):
        p, q  = "amz", 'amz'

        self.assertEqual(3, solution(p, q))



if __name__ == '__main__':
    unittest.main()
