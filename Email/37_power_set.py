"""
A set is a collection of distinct things.
For example the set of [1,1,2,3,3,4,4] => [1,2,3,4]

The power set of a set is the collection of all subsets of a set. Write a function that, given a set, generates its power set.

For example, given the set [1,2,3], it should return [ [ ], [1], [2], [3], [1,2], [1,3], [2,3], [1,2,3]].

You may use an array to represent a set. 
"""


def powerSet(set):
    res = [[]]
    for num in set:
        resLen = len(res)
        for i in range(resLen):
            curSet = res[i].copy()
            curSet.append(num)
            res.append(curSet)
    return res
