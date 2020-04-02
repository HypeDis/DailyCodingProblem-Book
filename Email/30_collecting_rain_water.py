""" 
You are given an array of non-negative integers that represents a two-dimensional 
elevation map where each element is unit-width wall and the integer is the height. 
Suppose it will rain and all spots between two walls get filled up.

Compute how many units of water remain trapped on the map in O(N) time and O(1) space.

For example, given the input [2, 1, 2], we can hold 1 unit of water in the middle.

Given the input [3, 0, 1, 3, 0, 5], we can hold 3 units in the first index, 2 in the second, 
and 3 in the fourth index (we cannot hold 5 since it would run off to the left), 
so we can trap 8 units of water. 
"""
'''
 __    __
|__|__|__|
|__|__|__|
[2,1,2]

            _
/          | |  _
/          | | | | 
/     _    | | | |
/    | |   | | | |
/    | |  _| | | |
/    | | | | | | |
/     3 0 1 6 0 5
'''

# at any given index we can collect as much water as min(lMax, rMax) - currentHeight
# with the 2 pointers we can always know the lMax for the left half and rMax  for the right half when we
# start from the outsides working in.
# if the left side has a smaller max we know that the maximum amount of water is bound by its max and vice versa


def collectWater(walls):
    if len(walls) < 2:
        return 0
    water = 0
    l, r = 0, len(walls) - 1
    lMax, rMax = 0, 0

    while l < r:
        lMax = max(lMax, walls[l])
        rMax = max(rMax, walls[r])
        if lMax < rMax:
            water += lMax - walls[l]
            l += 1
        else:
            water += rMax - walls[r]
            r -= 1
    return water


assert collectWater([]) == 0
assert collectWater([1]) == 0
assert collectWater([2, 1, 2]) == 1
assert collectWater([0, 1, 3, 0, 3]) == 3
assert collectWater([3, 0, 1, 3, 0, 5]) == 8
assert collectWater([3, 0, 4, 1, 5, 3]) == 6
