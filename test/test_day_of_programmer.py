from day_of_programmer import solution, is_leap, get_calendar
import unittest

class MyTestCase(unittest.TestCase):
    def test_is_leap(self):

        tpls = [
                 (1984, True),
                 (2017, False),
                 (2016, True),
                 (1800, True)

                 ]
        for expected, res in tpls:
            calname = get_calendar(expected)
            self.assertEqual(res, is_leap(expected, calname), expected)


    def test_julian_year(self):
        res = solution(1917)
        print(res)

    def test_julian_year(self):
        res = solution(1800)
        print(res)

    def test_2017(self):
        res = solution(2017)
        print(f'|{res}')


if __name__ == '__main__':
    unittest.main()

