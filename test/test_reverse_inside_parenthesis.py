import unittest
from reverse_inside_parenthesis import solution

class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEquals(solution("h(el)lo)"), "h(le)lo")

    def test_two(self):
        self.assertEquals(solution("a ((d e) c b)") , "a (b c (d e))")

    def test_three(self):
        self.assertEqual(solution("one (two (three) four)"), "one (ruof (three) owt)")

    def test_four(self):
        self.assertEqual(solution("one (ruof ((rht)ee) owt)"), "one (two ((thr)ee) four)")

if __name__ == '__main__':
    unittest.main()
