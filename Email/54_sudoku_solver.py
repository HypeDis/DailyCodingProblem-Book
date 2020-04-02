"""  
Sudoku is a puzzle where you're given a partially-filled 9 by 9 grid with digits. 
The objective is to fill the grid with the constraint that every col, column, 
and box (3 by 3 subgrid) must contain all of the digits from 1 to 9.
Implement an efficient sudoku solver.
"""

board = [["5", "3", ".", ".", "7", ".", ".", ".", "."],
         ["6", ".", ".", "1", "9", "5", ".", ".", "."],
         [".", "9", "8", ".", ".", ".", ".", "6", "."],
         ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
         ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
         ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
         [".", "6", ".", ".", ".", ".", "2", "8", "."],
         [".", ".", ".", "4", "1", "9", ".", ".", "5"],
         [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
"""  
loop through the entire array
for each empty spot check 1-9
if not valid backtrack
if valid continue

"""


def solveSudoku(board):
    helper(board, 0, 0)
    return board


def helper(board, row, col):
    # gone past the board constraints
    if row == len(board):
        return True
    # move down a row and start from
    if col > len(board[0]) - 1:
        return helper(board, row + 1, 0)
    # skip pre-filled board elements
    if board[row][col] != '.':
        return helper(board, row, col + 1)

    for i in range(1, 10):
        board[row][col] = str(i)
        if colIsValid(board, row, col) and rowIsValid(
                board, row, col) and boxIsValid(board, row, col):
            validBoard = helper(board, row, col + 1)
            if validBoard:
                return True
            else:
                board[row][col] = '.'
        else:
            board[row][col] = '.'
    return False


def colIsValid(board, row, col):
    curVal = board[row][col]
    for i in range(9):
        if i == row:
            continue
        if board[i][col] == curVal:
            return False
    return True


def rowIsValid(board, row, col):
    curVal = board[row][col]
    for i in range(9):
        if i == col:
            continue
        if board[row][i] == curVal:
            return False
    return True


def boxIsValid(board, row, col):
    curVal = board[row][col]
    rowRange = None
    colRange = None
    if row >= 6:
        rowRange = [6, 8]
    elif row >= 3:
        rowRange = [3, 5]
    else:
        rowRange = [0, 2]

    if col >= 6:
        colRange = [6, 8]
    elif col >= 3:
        colRange = [3, 5]
    else:
        colRange = [0, 2]

    for i in range(rowRange[0], rowRange[1] + 1):
        for j in range(colRange[0], colRange[1] + 1):
            if i == row and j == col:
                continue
            if board[i][j] == curVal:
                return False

    return True


solveSudoku(board)

print('\n'.join([','.join(row) for row in board]))