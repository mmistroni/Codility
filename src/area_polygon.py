#https://www.codewars.com/kata/5a58ca28e626c55ae000018a

import math


def area_of_inscribed_polygon(circle_radius, number_of_sides):
    return (number_of_sides * circle_radius**2) * math.sin(2 * math.pi / number_of_sides) / 2