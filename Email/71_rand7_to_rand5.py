""" 
Using a function rand7() that returns an integer from 1 to 7 (inclusive) with uniform probability, implement a function rand5() that returns an integer from 1 to 5 (inclusive). 
"""
from random import randint, random


def randInit(range):
    def rand():
        return randint(1, range)

    return rand


rand7 = randInit(7)


def rand5():
    while (True):
        randomNum = rand7()
        if randomNum <= 5:
            return randomNum


ghettoGraph = [[] for _ in range(5)]
for i in range(500):
    randNum = rand5()
    ghettoGraph[randNum - 1].append('*')

ghettoString = '\n'.join([''.join(row) for row in ghettoGraph])
print(ghettoString)
