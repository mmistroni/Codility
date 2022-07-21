'''
https://app.codility.com/c/run/certJBGFBJ-3RBSTGTPDCUD4WV7/

There are N points (numbered from 0 to N−1) on a plane. Each point is colored either red ('R') or green ('G'). The K-th point is located at coordinates (X[K], Y[K]) and its color is colors[K]. No point lies on coordinates (0, 0).

We want to draw a circle centered on coordinates (0, 0), such that the number of red points and green points inside the circle is equal. What is the maximum number of points that can lie inside such a circle? Note that it is always possible to draw a circle with no points inside.

Write a function:

def solution(X, Y, colors)

that, given two arrays of integers X, Y and a string colors, returns an integer specifying the maximum number of points inside a circle containing an equal number of red points and green points.

Examples:

1. Given X = [4, 0, 2, −2], Y = [4, 1, 2, −3] and colors = "RGRR", your function should return 2. The circle contains points (0, 1) and (2, 2), but not points (−2, −3) and (4, 4).


2. Given X = [1, 1, −1, −1], Y = [1, −1, 1, −1] and colors = "RGRG", your function should return 4. All points lie inside the circle.

Given X = [1, 0, 0], Y = [0, 1, −1] and colors = "GGR", your function should return 0. Any circle that contains more than zero points has an unequal number of green and red points.

Given X = [5, −5, 5], Y = [1, −1, −3] and colors = "GRG", your function should return 2.

Given X = [3000, −3000, 4100, −4100, −3000], Y = [5000, −5000, 4100, −4100, 5000] and colors = "RRGRG", your function should return 2.

'''
import math
def distanceFromCentre(tpl):
    x = tpl[0]
    y = tpl[1]
    return (x, y, tpl[2], math.sqrt(x**2 + y**2))

def evaluate(points):
    redCount = 0
    greenCount = 0
    idx = 0
    distances = set()
    lastEqual = 0;
    for idx, tpl in enumerate(points):
        #excluding same points
        _, _, flag, distance = tpl
        print(f'Current Dist:{distance}, Distances:{distances}')
        if 'G' in flag:
            greenCount +=1
        else:
            redCount +=1
        if greenCount == redCount:
            lastEqual = greenCount +redCount

    if lastEqual % 2 == 0:
        return lastEqual
    return 0

def solution(X, Y, colors):
    # write your code in Python 3.6
    # Tentative. sort the points from closest to origin and keep track of colors
    # loop thru all points and keep track of how many greens and how many reds
    # We need to have even green and even red
    whole =  zip(X, Y, colors)

    distances = map(lambda tpl: distanceFromCentre(tpl), whole)
    sorted_points = sorted(distances, key= lambda x: x[3])

    return evaluate(list(sorted_points))
