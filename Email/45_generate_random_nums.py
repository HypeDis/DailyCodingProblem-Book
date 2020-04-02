""" 
Using a function rand5() that returns an integer from 1 to 5 (inclusive) 
with uniform probability, implement a function rand7() 
that returns an integer from 1 to 7 (inclusive). 
"""
from random import randrange, random, randint
import math


def randomRange(range):
    def rand():
        return randint(1, range)
        # return randrange(1, range + 1, 1)
        # return math.trunc(random() * range) + 1

    return rand


rand5 = randomRange(5)
rand7 = randomRange(7)

print(rand5())
print(rand7())
