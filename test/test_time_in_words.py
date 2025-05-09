import unittest
from src.time_in_words import solution

class MyTestCase(unittest.TestCase):
    def test_something(self):

        resultTuple = [('5:00', "five o' clock"),
                       ('5:01', "one minute past five"),
                       ('5:10', "ten minutes past five"),
                       ('5:15', "quarter past five"),
                       ('5:30', "half past five"),
                       ('5:40', "twenty minutes to six"),
                       ('5:45', "quarter to six"),
                       ('5:47', "thirteen minutes to six"),
                       ('5:28', "twenty eight minutes past five")
                 ]

        for time_str, expected in resultTuple:
            h, m = time_str.split(':')
            res = solution(int(h), int(m))
            self.assertEqual(expected, res,  '{res} should be:{expected}')




if __name__ == '__main__':
    unittest.main()
