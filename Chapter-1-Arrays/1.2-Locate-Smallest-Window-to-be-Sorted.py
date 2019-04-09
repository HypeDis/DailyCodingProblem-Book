""" 
Given an array of integers that are out of order, determine the bounds of the smallest window that must be sorted 
in order for the entire array to be sorted. For example, given [3, 7, 5, 6, 9], you should return (1,3).count

 """

#  my solution
# two pointers
# left pointer moves until it hits out of order element. moves backwards until it finds a value smaller than that element.
# right pointer does the same thing but backwards. The window is between those two indexes (exclusive).
# if the pointers are at the same spot sort entire array
# if left pointer reaches the end, array is already sorted.


import testData

myArray = testData.myArray

# anything smaller than and to the right of max_seen must be out of order
# anything bigger than and to the left of min_seen must be out of order
def solutionWindow(arr):
    left, right = None, None
    n = len(arr)
    max_seen, min_seen = -float("inf"), float("inf")

    for i in range(n):
        max_seen = max(max_seen, arr[i])
        if arr[i] < max_seen:
            right = i
    # syntax for range: range(start, stop(exclusive), step)
    for i in range(n - 1, -1, -1):
        min_seen = min(min_seen, arr[i])
        if arr[i] > min_seen:
            left = i
    return left, right


# if answer is (None, None), array is sorted

print("solutionWindow", solutionWindow(myArray))
