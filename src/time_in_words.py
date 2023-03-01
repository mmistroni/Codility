#https://www.hackerrank.com/challenges/the-time-in-words/problem
from datetime import datetime
import logging

time_to_word_dict = {0:'zero', 1:'one', 2:'two', 3:'three', 4:'four', 5:'five', 6 :'six', 7:'seven', 8 :'eight', 9:'nine', 10:'ten',
11:'eleven', 12:'twelve', 13:'thirteen', 14:'fourteen', 15:'quarter', 16 :'sixteen', 17:'seventeen', 18 :'eighteen', 19:'nineteen', 20:'twenty',
21:'twentyone', 22:'twentytwo', 23:'twentythree', 24:'twentyfour', 25:'twentyfive', 26 :'twentysix', 27:'twentyseven',
                      28 :'twentyeight', 29:'twentynine', 30:'half',

}

def solution(input_str):
    hr = None
    min = None
    try:
        dt = datetime.strptime(input_str, '%H:%M')
        min = dt.minute
        hr = dt.hour
    except Exception as e:
        raise e

    return_hr = hr % 12
    return_min = min

    hr_string = time_to_word_dict[return_hr]


    if min == 0:
        return f"{hr_string} o'clock"
    else:

        conjunction = 'to' if return_min > 30 else 'past'
        real_min = return_min % 30
        min_str = time_to_word_dict[real_min]

        minute_suffix = ''

        if min != 15 and min != 30:
            if real_min % 30 >=10:
                minute_suffix = ' minutes'
            else:
                minute_suffix = ' minute'
        else:
            min_str = time_to_word_dict[min]


        return f'{min_str}{minute_suffix} {conjunction} {hr_string}'


