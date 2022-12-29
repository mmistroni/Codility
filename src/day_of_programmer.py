#https://www.hackerrank.com/challenges/day-of-the-programmer/problem?isFullScreen=true

day_of_programmer = 256

calendar_dict = {'Julian' :  ([29, 28, 31, 29, 31, 29, 31, 29],
                              [29, 23, 27, 31, 29, 31, 29, 31, 29]),
                 'Interim':  ([31, 14, 31, 30, 31, 30, 31, 31],
                              [31, 14, 31, 30, 31, 30, 31, 31]),
                 'Gregorian' : ([31, 28, 31, 30, 31, 30, 31, 31],
                                [31, 29, 31, 30, 31, 30, 31, 31])}



def is_leap(year, key):
    if 'Gregorian' in key:
        if year % 400 == 0:
            return True
        if year % 4 == 0 and year % 100 !=0:
            return True
        return False
    elif 'Julian' in key:
        return year % 4 == 0
    return False


def get_calendar(year):
    if year <=1917:
        return 'Julian'
    elif year == 1918:
        return 'Interim'
    return 'Gregorian'


def solution(year):

    calname = get_calendar(year)

    tpls = calendar_dict.get(calname)

    if is_leap(year, calname):
        item  = tpls[1]
    else:
        item = tpls[0]

    all_dt = 256 - sum(item)

    return f'{all_dt}.9.{year}'




    prog_day = 256
