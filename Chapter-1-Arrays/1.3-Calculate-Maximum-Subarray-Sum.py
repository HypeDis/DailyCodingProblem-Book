# Given an array of numbers, find the maximum sum of any contiguous subarray of the given array. For example, given the array [34,-50, 42, 14,-5,86], the maximum sum would be 137, since we would take elements 42, 14, -5, and 86. Given the array [-5, -1, -8, -9], the maximum sum would be 0, since we would choose not to take any elements.
# Do this in O(n) time.

# Follow-up: What if the elements can wrap around? For example, given [8, -1, 3, 4], return 15, as we choose the numbers 3,4, and 8 where the 8 is obtained from wrapping around.
from functools import reduce

# myArray = [8, -1, 3, 4]  # should be 15 with wrapping

# any maximum sum will be between two positive numbers.
# find all positive vale\ue indexes (if none exist return 0)
# find the sum between all positive indexes
# find the maximum sum

""" def myMaxSubArray(nums):
    n = len(nums)

    # find the index of all positive integers
    positiveIdxs = []
    for i in range(n):
        if nums[i] > 0:
            positiveIdxs.append(i)

    if not positiveIdxs:
        return 0
    sums = []
    for idx1 in positiveIdxs:
        for idx2 in positiveIdxs:
            reduceArr = []
            # join 2 slices of nums array together if wrapping back around
            if idx2 < idx1:
                reduceArr = nums[: idx2 + 1] + nums[idx1:]
            else:
                reduceArr = nums[idx1 : idx2 + 1]

            # sums.append(reduce(lambda x, y: x + y, reduceArr))
            sums.append(sum(reduceArr))

    # search for the max sum
    maxSum = 0
    for currentSum in sums:
        if currentSum > maxSum:
            maxSum = currentSum

    return maxSum
 """

# what if we want to include negative sums?

# print(myMaxSubArray(myArray))

myArray = [34, -50, 42, 14, -5, 86]


def maxSubArray(nums):
    maxSum, maxEndingHere = -float("inf"), -float("inf")
    for num in nums:
        maxEndingHere = max(num, maxEndingHere + num)
        maxSum = max(maxSum, maxEndingHere)
    return maxSum


def minSubArray(nums):
    minSum, minEndingHere = float("inf"), float("inf")
    for num in nums:
        minEndingHere = min(num, minEndingHere + num)
        minSum = min(minSum, minEndingHere)
    return minSum


def maxCircularSubArray(nums):
    maxCircularSum = sum(nums) - minSubArray(nums)
    return max(maxSubArray(nums), maxCircularSum)


print(maxCircularSubArray(myArray))
