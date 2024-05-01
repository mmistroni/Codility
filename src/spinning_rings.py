#https://www.codewars.com/kata/59afff65f1c8274f270020f5/train/python

def spinning_rings(inner_max, outer_max):
    counter = 0
    start1  = 0
    start2 = 0
    while True:
        counter +=1
        start1 = start1 -1 if start1 > 0 else inner_max
        start2 = start2 + 1 if start2 < outer_max else 0
        if start1 == start2:
            return counter