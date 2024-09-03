#https://www.codewars.com/kata/66cdc6ab9e7a9f009e0ca8f6Problem Description:
'''
A snail is crawling along a rubber band that has an initial length of x units. The snail moves at a constant speed of y units per minute. As the snail crawls from the left end of the rubber band to the right end, the rubber band increases in length from the right side every minute, adding z units to its length.

The question is: Will the snail be able to reach the right end of the rubber band within 1 year?

Parameters:

x: Initial length of the rubber band (in units), where 0.01 ≤ x ≤ 1,000,000.
y: Speed of the snail (in units per minute), where 0.01 ≤ y ≤ 1,000,000.
z: Amount by which the rubber band increases in length every minute (in units), where 0.01 ≤ z ≤ 1,000,000.
'''


year_mins = 60 * 24 * 365


def can_crawl(x, y, z ):

    # Not working. we need to calculate this to avoid looping.

    if  z > y:
        return False
    else:
        progress = y - z
        return x / progress < year_mins
