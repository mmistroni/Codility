import unittest

from migratory_birds import solution
class MyTestCase(unittest.TestCase):
    def test_something(self):
        tester = [1,1,2,2,3]
        self.assertEqual(1, solution(tester))

    def test_something2(self):
        tester = [1, 4, 4, 4, 5, 3]
        self.assertEqual(4, solution(tester))


if __name__ == '__main__':
    unittest.main()
