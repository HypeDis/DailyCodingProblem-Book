"""  
A knight's tour is a sequence of moves by a knight on a chessboard such that 
all squares are visited once.

Given N, write a function to return the number of knight's tours on an N by N chessboard. 
"""


# brute force solution with backtracking
def knightsTour(n):
    pass
    board = [[None] * n for _ in range(n)]
    tours = 0
    for y in range(len(board)):
        for x in range(len(board[0])):
            print(x, y)
            tours += helper(board, 0, n**2 - 1, x, y)
    return tours


def helper(board, numMoves, maxMoves, x, y):
    if x < 0 or x > len(board[0]) - 1 or y < 0 or y > len(board) - 1:
        return 0
    if (board[y][x] == 1):
        return 0
    if numMoves == maxMoves:
        return 1

    board[y][x] = 1

    tours = helper(board, numMoves + 1, maxMoves, x - 2, y + 1) + helper(
        board, numMoves + 1, maxMoves, x - 2,
        y - 1) + helper(board, numMoves + 1, maxMoves, x - 1, y + 2) + helper(
            board, numMoves + 1, maxMoves, x + 1, y + 2) + helper(
                board, numMoves + 1, maxMoves, x + 2, y + 1) + helper(
                    board, numMoves + 1, maxMoves, x + 2, y - 1) + helper(
                        board, numMoves + 1, maxMoves, x + 1, y - 2) + helper(
                            board, numMoves + 1, maxMoves, x - 1, y - 2)
    board[y][x] = None
    return tours


print(knightsTour(5))
