import unittest
from valleys import solution

class MyTestCase(unittest.TestCase):
    def test_something(self):
        steps = 8
        path = "UDDDUDUU"
        self.assertEqual(1, solution(steps, path))

    def test_something2(self):
        steps = 12
        path = "DDUUDDUDUUUD"
        self.assertEqual(2, solution(steps, path))

if __name__ == '__main__':
    unittest.main()
