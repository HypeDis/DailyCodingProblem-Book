""" 
You have an N by N board. Write a function that, given N, returns the number of possible arrangements 
of the board where N queens can be placed on the board without 
threatening each other, i.e. no two queens share the same row, column, or diagonal. 
"""
'''
n = 1 
[q] // 1 possible way 
n = 2 
[q,0] 
[0,0]

[0,q]
[0,0] // 0 possible ways

[q,0,0] [0,q,0] [0,0,q]
[0,0,q] [0,0,0] [q,0,0]
[0,0,0] [0,0,q] [0,0,0] // 0 possible ways

for each row check the column, and diagonals above it
'''


def nQueens(n):
    board = [[0] * n for _ in range(n)]
    return helper(0, board)


def helper(row, board):
    if row > len(board) - 1:
        return 1
    possibilities = 0
    for col in range(len(board[0])):
        if not hasCollision(row, col, board):
            board[row][col] = 'q'
            possibilities += helper(row + 1, board)
            board[row][col] = 0
    return possibilities


def hasCollision(y, x, board):
    # check column
    left = x
    right = x
    while y > 0:
        if board[y - 1][x] == 'q':
            return True
        if left > 0 and board[y - 1][left - 1] == 'q':
            return True
        if right < len(board[0]) - 1 and board[y - 1][right + 1] == 'q':
            return True

        y -= 1
        left -= 1
        right += 1
    return False

    # check diagonals


print(nQueens(4))

# time complexity O(n!) for every queen placed the next queen has 1 less space it can go (the column the previous piece is on)
# space complexity O(n) the board size