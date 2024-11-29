import unittest

from src.grading_students import grade

class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(85, grade(84))
        self.assertEqual(57, grade(57))
        self.assertEqual(29, grade(29))


if __name__ == '__main__':
    unittest.main()
