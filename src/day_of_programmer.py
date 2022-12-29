#https://www.hackerrank.com/challenges/day-of-the-programmer/problem?isFullScreen=true

days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def is_leap(year):
    if year % 400 == 0:
        return True
    if year % 4 == 0 and year % 100 !=0:
        return True
    return False

def is_gregorian(year):
    return False


def solution(year):
    if is_leap(year):
        days[1] = 29
    

    prog_day = 256
