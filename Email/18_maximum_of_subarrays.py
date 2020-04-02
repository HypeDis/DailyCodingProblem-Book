""" 
Given an array of integers and a number k, where 1 <= k <= length of the array, 
compute the maximum values of each subarray of length k.

For example, given array = [10, 5, 2, 7, 8, 7] and k = 3, we should get: [10, 7, 8, 8], since:

    10 = max(10, 5, 2)
    7 = max(5, 2, 7)
    8 = max(2, 7, 8)
    8 = max(7, 8, 7)

Do this in O(n) time and O(k) space. You can modify the input array in-place 
and you do not need to store the results. 
You can simply print them out as you compute them.
"""

from collections import deque


def maximums(arr, k):
    maxes = []
    # largest value is always index 0
    localMaxes = deque([])
    left = 0
    right = 0

    # edge cases
    if not arr:
        return None
    if (len(arr) < k):
        return max(arr)

    # sliding window
    for i in range(len(arr)):
        # prune localMaxes if value is no longer in the window
        if right - left == k:
            if arr[left] == localMaxes[0]:
                localMaxes.popleft()
                left += 1
        # remove all values from localMaxes that are smaller than current right most value
        while localMaxes and localMaxes[-1] < arr[right]:
            localMaxes.pop()
        # add the current value to the localMaxes
        localMaxes.append(arr[right])

        if i >= k - 1:
            maxes.append(localMaxes[0])
        right += 1

    return maxes


arr = [10, 5, 2, 7, 8, 7]
k = 3

print(maximums(arr, k))
print(maximums([1], 9))
