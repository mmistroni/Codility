import unittest

from maximize import solution
class MyTestCase(unittest.TestCase):
    def test_something(self):

        #A = [-3, 1, 2, -2, 5, 6 ]
        A = [-5, 5, -5, 4]
        self.assertEqual(125, solution(A))


if __name__ == '__main__':
    unittest.main()
