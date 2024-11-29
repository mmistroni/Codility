import unittest
from src.hackerrank_in_string import solution

class MyTestCase(unittest.TestCase):

    def test_something(self):
        strings = [('haacckkerrannkk', 'YES'),
                   ('haacckkerannk', 'NO'),
                    ('hccaakkerrannkk','NO'),
                     ('hereiamstackerrank', 'YES'),
                      ('hackerworld', 'NO')

                   ]


        for test, expected in strings:
            self.assertEquals(expected, solution(test))

if __name__ == '__main__':
    unittest.main()
