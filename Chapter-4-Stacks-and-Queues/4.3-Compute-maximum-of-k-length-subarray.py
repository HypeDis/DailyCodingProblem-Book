""" 

Given an array of integers and a number k, where 1 <= k <= array length, compute the maximum values of each subarray of length k.

For example, let's say the array is [10, 5, 2 , 7, 8, 7] and k = 3. We should get [10, 7, 8 , 8], since :

10 = max(10, 5, 2)
7 = max(5 , 2, 7)
8 = max(2, 7 , 8)
8 = max(7, 8, 7) 

O(n) time O(k) space

"""

myList = [10, 5, 2, 7, 8, 7]

from collections import deque


def maxOfSubArrays(lst, k):
    q = deque()
    maxList = []

    # load in the first window
    for i in range(k):
        while q and lst[i] >= lst[q[0]]:
            q.pop()
        q.append(i)
    maxList.append(lst[q[0]])
    for i in range(k, len(lst)):
        if q[0] <= i - k:
            q.popleft()
        while q and lst[i] >= lst[q[0]]:
            q.pop()
        q.append(i)
        maxList.append(lst[q[0]])
    return maxList


print(maxOfSubArrays(myList, 3))