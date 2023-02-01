import unittest
from beautiful_triplets import solution

class MyTestCase(unittest.TestCase):
    def test_something(self):

        inarray = [2,2,3,4,5]

        self.assertEqual(3, solution(inarray))


if __name__ == '__main__':
    unittest.main()
