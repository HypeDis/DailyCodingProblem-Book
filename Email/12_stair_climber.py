""" 
There exists a staircase with N steps, and you can climb up either 1 or 2 steps at a time. 
Given N, write a function that returns the number of unique ways you can climb the staircase. 
The order of the steps matters.

For example, if N is 4, then there are 5 unique ways:

    1, 1, 1, 1
    2, 1, 1
    1, 2, 1
    1, 1, 2
    2, 2

What if, instead of being able to climb 1 or 2 steps at a time, 
you could climb any number from a set of positive integers X? 
For example, if X = {1, 3, 5}, you could climb 1, 3, or 5 steps at a time. 
"""


def stairClimber(n):
    if n == 0:
        return 1

    if n < 0:
        return 0

    return stairClimber(n - 1) + stairClimber(n - 2)


# print(stairClimber(4))

memo = {}


def stairMemo(n):

    if n == 1:
        memo[1] = 1

    if n == 0:
        memo[0] = 1
    if n in memo:
        return memo[n]

    memo[n] = stairMemo(n - 1) + stairMemo(n - 2)
    return memo[n]


print(stairMemo(4))