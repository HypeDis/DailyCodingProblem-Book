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

# yapf: disable
import time;
# yapf: enable

#  my solution doesn't work if there are duplicate values
def myWindow(arr):
    leftVal = arr[0]
    rightVal = arr[len(arr) - 1]

    leftPointer, rightPointer = 0, len(arr) - 1
    isMovingLP, isMovingRP = True, True

    while (
        leftPointer < len(arr) - 1 and rightPointer > 0 and (isMovingLP or isMovingRP)
    ):
        # break conditions
        if leftPointer > rightPointer:
            return "sorted"
        # move left pointer
        if arr[leftPointer] < arr[leftPointer + 1]:
            leftPointer += 1
        else:
            isMovingLP = False
        # move right pointer
        if arr[rightPointer] > arr[rightPointer - 1]:
            rightPointer -= 1
        else:
            isMovingRP = False
    leftPointer += 1
    rightPointer -= 1
    # backtrack pointers
    leftBound = arr[leftPointer]
    rightBound = arr[rightPointer]

    while leftPointer != 0 and arr[leftPointer - 1] > leftBound:
        leftPointer -= 1
    while rightPointer != len(arr) - 1 and arr[rightPointer + 1] < rightBound:
        rightPointer += 1

    # edge case where the min value is all the way right, or the max value is all the way left
    while leftPointer > 0 and arr[leftPointer - 1] > arr[rightPointer]:
        leftPointer -= 1
    while rightPointer < len(arr) - 1 and arr[rightPointer + 1] < arr[leftPointer]:
        rightPointer += 1
    return (leftPointer, rightPointer)


# myArray = [1, 2, 3, 6, 5, 7, 4]
# myArray = [3, 7, 5, 6, 9, 1]
import testData

myArray = testData.myArray
myArray = [3, 4, 5, 3, 2, 3]
mySortedArray = testData.mySortedArray

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
    # range(start, stop(exclusive), step)
    for i in range(n - 1, -1, -1):
        min_seen = min(min_seen, arr[i])
        if arr[i] > min_seen:
            left = i
    return left, right


myStart = time.time()
print("myWindow", myWindow(myArray))
myEnd = time.time()
print("my time", str((myEnd - myStart) * 10 ** 6) + " ns")

solutionStart = time.time()
print("solutionWindow", solutionWindow(myArray))
solutionEnd = time.time()
print("solution time", str((solutionEnd - solutionStart) * 10 ** 6) + " ns")


print("\n")
myStart = time.time()
print("myWindow", myWindow(mySortedArray))
myEnd = time.time()
print("my time", str((myEnd - myStart) * 10 ** 6) + " ns")

solutionStart = time.time()
print("solutionWindow", solutionWindow(mySortedArray))
solutionEnd = time.time()
print("solution time", str((solutionEnd - solutionStart) * 10 ** 6) + " ns")
