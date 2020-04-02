"""
On our special chessboard, two bishops attack each other if they share the same diagonal. 
This includes bishops that have another bishop located between them, 
i.e. bishops can attack through pieces.

You are given N bishops, represented aw (row, column) tuples on a M by M chessboard. 
Write a function to count the number of pairs of bishops that attack each other. 
The ordering of the pair doesn't matter: (1, 2) is considered the same as (2, 1).

For example, given M = 5 and the list of bishops:

    (0, 0)
    (1, 2)
    (2, 2)
    (4, 0)

The board would look like this:

[b 0 0 0 0]
[0 0 b 0 0]
[0 0 b 0 0]
[0 0 0 0 0]
[b 0 0 0 0]

You should return 2, since bishops 1 and 3 attack each other, as well as bishops 3 and 4. 
"""
from math import factorial


def getAttacks(board):
    comb2 = combination(2)
    totalAttacks = 0
    bishopCount = 0
    for y in range(len(board) - 1):
        if y == 0:
            for x in range(len(board[0])):
                leftBishops = checkLeftDiagonal(board, x, y)
                if leftBishops > 1:
                    bishopCount += comb2(leftBishops)
                rightBishops = checkRightDiagonal(board, x, y)
                print('rightBishops', rightBishops)
                if rightBishops > 1:
                    bishopCount += comb2(rightBishops)
        else:
            leftEdgeCount = checkRightDiagonal(board, 0, y)
            rightEdgeCount = checkLeftDiagonal(board, len(board[0]) - 1, y)
            if leftEdgeCount > 1:
                bishopCount += comb2(leftEdgeCount)
            if rightEdgeCount > 1:
                bishopCount += comb2(rightEdgeCount)
    return bishopCount


def checkLeftDiagonal(board, x, y):
    count = 0
    if x < 0 or x > len(board[0]) - 1 or y > len(board) - 1:
        return 0
    if board[y][x] == 'b':
        count += 1
    return count + checkLeftDiagonal(board, x - 1, y + 1)


def checkRightDiagonal(board, x, y):
    count = 0
    if x < 0 or x > len(board[0]) - 1 or y > len(board) - 1:
        return 0
    if board[y][x] == 'b':
        count += 1
    return count + checkRightDiagonal(board, x + 1, y + 1)


def combination(groupSize):
    def getCombination(sampleSize):
        return factorial(sampleSize) / (factorial(groupSize) *
                                        factorial(sampleSize - groupSize))

    return getCombination


board = [['b', 0, 0, 0, 0], [0, 0, 'b', 0, 0], [0, 0, 'b', 0, 0],
         [0, 0, 0, 0, 0], ['b', 0, 0, 0, 0]]

board2 = [['b', 0, 0, 0, 0], [0, 'b', 'b', 0, 0], [0, 0, 'b', 0, 0],
          [0, 0, 0, 0, 0], ['b', 0, 0, 0, 'b']]
print(getAttacks(board))
print(getAttacks(board2))
