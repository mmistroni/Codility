import unittest

from Codility.src.counting_elements import solution
class MyTestCase(unittest.TestCase):
    def test_something(self):
        A = [3 ,4, 4, 6, 1, 4, 4]

        expected = [3, 2, 2, 4, 2]
        self.assertEqual(expected, solution(5, A))  # add assertion here


if __name__ == '__main__':
    unittest.main()
