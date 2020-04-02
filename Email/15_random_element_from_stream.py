""" 
Given a stream of elements too large to store in memory, 
pick a random element from the stream with uniform probability.[]
"""

# pick a random number and access the data in that index.
# swap that data with the front most available slot in the stream
# keep track of used slots, shrinking the range as more data is accessed

from random import random

nextAvailableSlot = 0
stream = [1, 2, 3, 4, 5, 6, 7]


def getRandom(stream):
    global nextAvailableSlot
    size = len(stream)
    sRange = size - nextAvailableSlot
    rand = int(random() * sRange + nextAvailableSlot)

    data = stream[rand]
    stream[nextAvailableSlot], stream[rand] = stream[rand], stream[
        nextAvailableSlot]
    nextAvailableSlot += 1
    return data


print(getRandom(stream))
print(getRandom(stream))
print(getRandom(stream))
print(getRandom(stream))
print(getRandom(stream))
print(getRandom(stream))
print(getRandom(stream))