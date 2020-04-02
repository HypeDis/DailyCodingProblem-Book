"""  
An sorted array of integers was rotated an unknown number of times.

Given such an array, find the index of the element in the array in faster than linear time. 
If the element doesn't exist in the array, return null.

For example, given the array [13, 18, 25, 2, 8, 10] and the element 8, 
return 4 (the index of 8 in the array).

You can assume all the integers in the array are unique. 
"""

# use binary search
# if number is between left and mid move right to mid - 1
# if number is between mid and right move left to mid + 1


def findNumber(nums, target):
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid

        if (nums[mid] > target
                and nums[left] <= target) or (nums[left] >= target
                                              and nums[mid] < target):
            right = mid - 1
        else:
            left = mid + 1
    return None


nums = [13, 18, 25, 2, 8, 10]
print(findNumber(nums, 8))
print(findNumber(nums, 13))
print(findNumber(nums, 10))
