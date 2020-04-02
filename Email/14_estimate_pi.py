'''
The area of a circle is defined as πr^2. 
Estimate π to 3 decimal places using a Monte Carlo method.

Hint: The basic equation of a circle is x^2 + y^2 = r^2
'''

# a circle of radius 0.5 inscribes a square of length 1
# pi * r^2  = pi/4 when r = 0.5
# the ratio of their areas is pi/4 : 1

# find points inside circle and points inside square
from random import random
from decimal import *
from sys import maxsize


def estimatePi(runs):
    inSquare = 0
    inCircle = 0

    for i in range(runs):
        randX = random() / 2
        randY = random() / 2
        inSquare += 1
        if randX**2 + randY**2 <= 0.5**2:
            inCircle += 1

    pi = 4 * (inCircle / inSquare)
    return round(pi, 3)


print(estimatePi(999999))
