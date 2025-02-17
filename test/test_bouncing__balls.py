from src.bouncing_balls import bouncing_ball
import unittest


class MyTestCase(unittest.TestCase):
    sample_test_cases = [
        ('Simple example',
         ['DOWN', 'REPTILE', 'AMIDST', 'SOFA'],  # words
         ['DOWN', 'REPTILE', 'AMIDST', 'SOFA'],  # expected
         ),
        ('Example',
         ['DOWN', 'PLANE', 'AMIDST', 'REPTILE', 'SOFA', 'SOLAR', 'SILENCE', 'DOWN', 'MARKDOWN'],  # words
         ['DOWN', 'REPTILE', 'AMIDST', 'SOFA', 'SOLAR', 'PLANE', 'SILENCE', 'MARKDOWN'],  # expected
         ),
        ('Empty',
         [],  # words
         [],  # expected
         ),
    ]

    def test_one(self):
        res = bouncing_ball(2, 0.5, 1)
        self.assertEqual(1, res)

    def test_two(self):

        res = bouncing_ball(3, 0.66, 1.5)
        self.assertEqual(3, res)

    def test_three(self):
        rs = bouncing_ball(30, 0.66, 1.5)
        self.assertEqual(15, rs)

    def test_four(self):
        res = bouncing_ball(30, 0.75, 1.5)
        self.assertEqual(21, res)