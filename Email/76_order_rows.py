"""  
You are given an N by M 2D matrix of lowercase letters. 
Determine the minimum number of columns that can be removed to ensure that each row is ordered from top to bottom lexicographically. 
That is, the letter at each column is lexicographically later as you go down each row. 
It does not matter whether each row itself is ordered lexicographically.

For example, given the following table:
cba
daf
ghi
This is not ordered because of the a in the center. We can remove the second column to make it ordered:
ca
df
gi
So your function should return 1, since we only needed to remove 1 column.
As another example, given the following table:
abcdef
Your function should return 0, since the rows are already ordered (there's only one row).
As another example, given the following table:
zyx
wvu
tsr
Your function should return 3, since we would need to remove all the columns to order it. """


def minColumnsRemoved(matrix):
    deleteCount = 0
    rows = len(matrix)
    cols = len(matrix[0])
    if not matrix or rows <= 1:
        return deleteCount

    for col in range(cols):
        for row in range(1, rows):
            prevChar = matrix[col][row - 1]
            curChar = matrix[col][row]
            if curChar < prevChar:
                deleteCount += 1
                break
    return deleteCount


m1 = [
    ['c', 'b', 'a'],
    ['d', 'a', 'f'],
    ['g', 'h', 'i'],
]
m2 = [['z', 'y', 'x'], ['w', 'v', 'u'], ['t', 's', 'r']]
m3 = [['a', 'z', 'd']]

assert minColumnsRemoved(m1) == 2
assert minColumnsRemoved(m2) == 3
assert minColumnsRemoved(m3) == 0
print('all tests passed')