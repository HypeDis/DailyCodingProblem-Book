""" 
Given an array of integers, return a new array such that each element at 
index i of the new array is the product of all the numbers in 
the original array except the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output would be 
[120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].

No division allowed.
"""


def productOfNums(nums):
    prefixTable = []
    suffixTable = []
    res = []

    for i in range(len(nums)):
        if i > 0:
            prefixTable.append(prefixTable[i - 1] * nums[i])
            suffixTable.append(suffixTable[i - 1] * nums[len(nums) - i - 1])
        else:
            prefixTable.append(nums[i])
            suffixTable.append(nums[len(nums) - 1])

    for i in range(len(nums)):
        pre = prefixTable[i - 1] if i > 0 else 1
        suf = suffixTable[len(nums) - i - 2] if i < len(nums) - 1 else 1
        res.append(pre * suf)

    return res


nums = [1, 2, 3, 4, 5]
assert productOfNums(nums) == [120, 60, 40, 30, 0], productOfNums(nums)
