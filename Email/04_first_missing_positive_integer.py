""" 
Given an array of integers, find the first missing positive integer in linear time and constant space. 
In other words, find the lowest positive integer that does not exist in the array. 
The array can contain duplicates and negative numbers as well.

For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.

You can modify the input array in-place. 
"""
'''
starting array
 *
[3, 4, -1, 1]
swap 3 and -1
  *
[-1, 4, 3, 1]
-1 => None
[None, 4, 3, 1]
next idx swap 4 and 1
       *
[None, 1, 3, 4]
swap 1 and None
[1, None, 3, 4]
all values are either None or in the right place

return the first None index + 1 => 2

3 cases for None:
value < 1
value > array size
value is duplicate
'''


def findFirstPositiveNumber(nums):
    size = len(nums)
    i = 0
    while i < size:
        val = nums[i]
        if val is None or val == i + 1:
            i += 1
            continue
        if val < 1 or val > size or val == nums[val - 1]:
            nums[i] = None
        else:
            nums[val - 1], nums[i] = nums[i], nums[val - 1]
    for i in range(len(nums)):
        if (nums[i] is None):
            return i + 1
    return len(nums) + 1


assert findFirstPositiveNumber([3, 4, -1, 1]) == 2
assert findFirstPositiveNumber([1, 2, 0]) == 3
