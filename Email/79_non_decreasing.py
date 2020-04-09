"""
Given an array of integers, write a function to determine whether the array could become non-decreasing by modifying at most 1 element.

For example, given the array [10, 5, 7], you should return true, since we can modify the 10 into a 1 to make the array non-decreasing.

Given the array [10, 5, 1], you should return false, since we can't modify any one element to get a non-decreasing array. 
"""


def canModify(arr):
    count = 0
    for i in range(len(arr) - 1, 0, -1):
        if arr[i] < arr[i - 1]:
            count += 1
            if count > 1:
                return False
            arr[i - 1] = arr[i]
    return True


assert canModify([10, 5, 7]) == True
assert canModify([10, 5, 1]) == False
assert canModify([1, 2, 3, 5, 4]) == True
assert canModify([1, 2, 6, 3, 5, 4]) == False
print('all tests passed')
