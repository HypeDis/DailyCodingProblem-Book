"""
Assume you have access to a function toss_biased() which returns 0 or 1 with a probability that's not 50-50 (but also not 0-100 or 100-0). You do not know the bias of the coin.

Write a function to simulate an unbiased coin toss.
"""
from random import random


def initializeToss(zeroBias):
    def toss():
        rand = random()
        if rand <= zeroBias:
            return 0
        return 1

    return toss



def estimateBias(runs, biasedFunc):
    zeroCount = 0
    for i in range(runs):
        toss = biasedFunc()
        if toss == 0:
            zeroCount += 1
    return zeroCount / runs


def initTossFair(biasedFunc):
    zeroBias = estimateBias(10000, biasedFunc)
    adjustment = abs(0.5 - zeroBias)

    def tossFair():
        toss = biasedFunc()
        if toss == 0 and zeroBias > 0.5:
            rand = random()
            target = adjustment / zeroBias
            if rand <= target:
                return 1
            else:
                return 0
        if toss == 1 and zeroBias < 0.5:
            rand = random()
            target = adjustment / (1 - zeroBias)
            if rand <= target:
                return 0
            else:
                return 1
        return toss

    return tossFair


tossBiased = initializeToss(.9)
tossFair = initTossFair(tossBiased)

print(estimateBias(100000, tossBiased))
print(estimateBias(100000, tossFair))
