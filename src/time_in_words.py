#https://www.hackerrank.com/challenges/the-time-in-words/problem
from datetime import datetime
import logging

time_to_word_dict = {0:'zero', 1:'one', 2:'two', 3:'three', 4:'four', 5:'five', 6 :'six', 7:'seven', 8 :'eight', 9:'nine', 10:'ten',
11:'eleven', 12:'twelve', 13:'thirteen', 14:'fourteen', 15:'quarter', 16 :'sixteen', 17:'seventeen', 18 :'eighteen', 19:'nineteen', 20:'twenty',
21:'twenty one', 22:'twenty two', 23:'twenty three', 24:'twenty four', 25:'twenty five', 26 :'twenty six', 27:'twenty seven',
                      28 :'twenty eight', 29:'twenty nine', 30:'half',

}

def solution(hr, min):

    return_hr = hr % 12
    return_min = min

    return_hr = return_hr + 1 if  return_min >30 else hr

    hr_string = time_to_word_dict[return_hr]


    if min == 0:
        return f"{hr_string} o' clock"
    else:

        conjunction = 'to' if return_min > 30 else 'past'
        adj_min = 60 - min if min > 30 else min


        minute_suffix = ''

        if adj_min != 15 and min != 30:
            wrd = time_to_word_dict[adj_min]
            min_str = wrd
            if adj_min > 1:
                minute_suffix = ' minutes'
            else:
                minute_suffix = ' minute'
        else:
            min_str = time_to_word_dict[adj_min]


        return f'{min_str}{minute_suffix} {conjunction} {hr_string}'


