""" 
Given a list of integers, write a function that returns the largest sum of 
non-adjacent numbers. Numbers can be 0 or negative.

For example, [2, 4, 6, 2, 5] should return 13, since we pick 2, 6, and 5. [5, 1, 1, 5] should return 10, 
since we pick 5 and 5.

Follow-up: Can you do this in O(N) time and constant space? 
"""
'''
[2,4,6,2,5]
2 + 6 + 5
2 + 2
2 + 5
'''

from collections import deque


def findMaxSum(nums):
    res = helper(nums, 0, 0, [])


def helper(nums, curIdx, sum, res):
    if curIdx > len(nums):
        res.append(sum)
        return
    for i in range(curIdx + 2, len(nums) + 2):
        helper(nums, i, sum + nums[curIdx], res)
        if curIdx > 0:
            helper(nums, i, nums[curIdx], res)
    return res


findMaxSum([2, 4, 6, 2, 5])

# time complexity: O(n!) ?
# space complexity: O(n/2) => O(n)
'''
[2,4,6,2,5]

i=0:
sums: 2
i = 1:
sums: 4
i = 2
num + max[i-2]
max[i -1]
'''


def maxSumDP(nums):
    maxSum = -float("inf")
    for i in range(len(nums)):
        if i < 2:
            maxSum = max(maxSum, nums[i])
            nums[i] = maxSum
        else:
            nums[i] = max(nums[i - 2] + nums[i], nums[i - 1])
            maxSum = max(nums[i], maxSum)
    return maxSum


# print('max sum dp', maxSumDP([2, 5, 6, 2, 5]))
# print('max sum dp', maxSumDP([5, 20, 15, 6]))
# print('max sum dp', maxSumDP([2, 5, 6, 2, 5]))

memo = {}


# using memoization
def maxSumMemo(nums, i):
    if (i == 0):
        memo[0] = nums[0]
        return memo[0]

    if (i == 1):
        memo[1] = max(nums[0], nums[i])
        return memo[1]

    if i in memo:
        return memo[i]

    memo[i] = max(maxSumMemo(nums, i - 1), maxSumMemo(nums, i - 2) + nums[i])

    return memo[i]


nums = [2, 5, 2, 5]
print('max sum dpr', maxSumMemo(nums, len(nums) - 1))


def maxSumIter(nums):
    prevOne, prevTwo, res = 0, 0, 0
    for i in range(len(nums)):
        if i == 0:
            prevOne = nums[0]
            res = prevOne
            continue
        if i == 1:
            prevTwo = nums[1]
            res = max(prevOne, prevTwo)
            continue
        res = max(prevTwo, prevOne + nums[i])
        prevOne = prevTwo
        prevTwo = res
    return res


nums = [2, 5, 2, 5]
print('max sum iterative', maxSumIter(nums))