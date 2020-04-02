"""
Given a list of integers, return the largest product 
that can be made by multiplying any three integers.

For example, if the list is [-10, -10, 5, 2], we should return 500, since that's -10 * -10 * 5.

You can assume the list has at least three integers.
"""


def getMaxProduct(nums):
    nums.sort()
    last = len(nums) - 1
    p1 = nums[0] * nums[1] * nums[last]
    p2 = nums[last] * nums[last - 1] * nums[last - 2]
    return max(p1, p2)


print(getMaxProduct([-10, -10, 5, 2]))
