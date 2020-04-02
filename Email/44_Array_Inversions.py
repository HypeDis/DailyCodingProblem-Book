"""
We can determine how "out of order" an array A is by counting the number of inversions it has. Two elements A[i] and A[j] form an inversion if A[i] > A[j] but i < j. That is, a smaller element appears after a larger element.

Given an array, count the number of inversions it has. Do this faster than O(N^2) time.

You may assume each element in the array is distinct.

For example, a sorted list has zero inversions. The array [2, 4, 1, 3, 5] has three inversions: (2, 1), (4, 1), and (4, 3). The array [5, 4, 3, 2, 1] has ten inversions: every distinct pair forms an inversion.
"""
'''
[5,4,3] [2,1]
[5,4]
[5][4] 4 < 5 so 1 inversion
[4,5] [3] 3 < 4 and 3 < 5 2 inversions
[2][1] 1 < 2 1 inversion
[3,4,5] [1,2] 1 < 3,4,5, 3 inversions 2 < 3,4,5 3 inversion
[1,2,3,4,5] 1 + 2 + 1 + 3 + 3 = 10 inversions


[ 2,4,1,3,5 ]
[2,4,1]
[2][4] 2 < 4 0 inversions

[2,4][1] 1 < 2,4 2 inversions
[3][5] 3 < 5 0 inversions
[1,2,4][3,5] 3 < 4 1 inversion
[1,2,3,4,5]

merge sort, when merging the arrays if we pick a number from the right array count how many are in the left array. Add that to the inversion count
'''


def getInversions(arr):
    if len(arr) == 1:
        return (arr, 0)

    half = len(arr) // 2 - 1
    (lh, lCount) = getInversions(arr[:half + 1])
    (rh, rCount) = getInversions(arr[half + 1:])
    count = lCount + rCount
    mergedArr = []
    i = 0
    j = 0
    while i < len(lh) and j < len(rh):
        if lh[i] < rh[j]:
            mergedArr.append(lh[i])
            i += 1
        else:
            count += len(lh)
            mergedArr.append(rh[j])
            j += 1
    if i < len(lh):
        mergedArr += lh
    if j < len(rh):
        mergedArr += rh
    return (mergedArr, count)


print(getInversions([5, 4, 3, 2, 1]))
print(getInversions([2, 4, 1, 3, 5]))
