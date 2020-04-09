"""  Given an array of numbers, find the length of the longest increasing subsequence in the array. 
The subsequence does not necessarily have to be contiguous.

For example, given the array [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15], 
the longest increasing subsequence has length 6: it is 0, 2, 6, 9, 11, 15. """


def longestSubsequence(nums):
    maxCount = 0
    for i in range(len(nums)):
        maxCount = max(maxCount, helper(nums, -float('inf'), i))
    return maxCount


def helper(nums, prevNum, curIdx):
    if curIdx >= len(nums) or nums[curIdx] <= prevNum:
        return 0

    curMax = 0
    for i in range(curIdx + 1, len(nums)):
        curMax = max(curMax, helper(nums, nums[curIdx], i))
    return 1 + curMax


print(
    longestSubsequence([0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]))

print(longestSubsequence([0, 1, 2, 4, 5]))
