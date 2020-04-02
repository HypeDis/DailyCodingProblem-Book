'''
 Given a list of numbers and a number k, 
 return whether any two numbers from the list add up to k.
For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
'''


def twoSum(nums, sum):
    seenNums = {}
    for num in nums:
        target = sum - num
        if target in seenNums:
            return True
        else:
            seenNums[num] = True
    return False


nums = [10, 15, 3, 7]
# 17 => True
# 12 => False
# 22 => True

nums2 = [4, 12, 8, 2]
# 20 => True
# 6 => True
# 8 => False

assert twoSum(nums, 17) == True
assert twoSum(nums, 12) == False
assert twoSum(nums, 22) == True

assert twoSum(nums2, 20) == True
assert twoSum(nums2, 6) == True
assert twoSum(nums2, 8) == False
