"""  
Given a N by M matrix of numbers, print out the matrix in a clockwise spiral.

For example, given the following matrix:

[[1,  2,  3,  4,  5],
 [6,  7,  8,  9,  10],
 [11, 12, 13, 14, 15],
 [16, 17, 18, 19, 20]]

You should print out the following:

1,2,3,4,5,10,15,20,19,18,17,16,11,6,7,8,9,14,13,12
"""


def traverseSpiral(arr):
    res = []
    x = 0
    y = 0
    total = len(arr) * len(arr[0])
    direction = 'r'
    for i in range(total):
        res.append(arr[y][x])
        arr[y][x] = None
        if direction == 'l':
            x -= 1
            if x < 0 or x > len(arr[0]) - 1 or not arr[y][x]:
                direction = 'u'
                x += 1
                y -= 1
        elif direction == 'r':
            x += 1
            if x < 0 or x > len(arr[0]) - 1 or not arr[y][x]:
                direction = 'd'
                x -= 1
                y += 1
        elif direction == 'd':
            y += 1
            if y < 0 or y > len(arr) - 1 or not arr[y][x]:
                direction = 'l'
                x -= 1
                y -= 1
        elif direction == 'u':
            y -= 1
            if y < 0 or y > len(arr) - 1 or not arr[y][x]:
                direction = 'r'
                x += 1
                y += 1
    return res


board = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15],
         [16, 17, 18, 19, 20]]

print(traverseSpiral(board))
