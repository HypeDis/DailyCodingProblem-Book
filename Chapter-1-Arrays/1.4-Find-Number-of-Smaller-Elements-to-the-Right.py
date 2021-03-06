""" 
Given an array of integers, return a new array where each element in the new array is the number of smaller elements to the right of that element in the original array.

example: [3,4,9, 6, 1] returns [1,1,2,1,0] 
"""

myArray = [3, 4, 9, 6, 1]

import bisect


def solutionSmallerToRight(nums):
    results = []
    seen = []
    # traverse list from right to left
    for num in reversed(nums):
        # find the index where num fits in. This index will indicate how many values to the right are smaller, since 'seen' is  a sorted array
        i = bisect.bisect_left(seen, num)
        results.append(i)
        # insert num in to 'seen' in the correct position
        bisect.insort(seen, num)
    # reverse the list and return it
    return list(reversed(results))

    # reversed() is O(n)
    # for loop is O(n)
    # bisect is O(logn) complexity
    # insort is O(n) time complexity
    # total time complexity is O(nlogn)
    # space complexity is S(n)


print(solutionSmallerToRight(myArray))
