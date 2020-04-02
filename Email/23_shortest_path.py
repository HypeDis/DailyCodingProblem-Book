"""  
You are given an M by N matrix consisting of booleans that represents a board. 
Each True boolean represents a wall. Each False boolean represents a tile you can walk on.

Given this matrix, a start coordinate, and an end coordinate, 
return the minimum number of steps required to reach the end coordinate from the start. 
If there is no possible path, then return null. You can move up, left, down, 
and right. You cannot move through walls. You cannot wrap around the edges of the board.

For example, given the following board:

[[f, f, f, f],
[t, t, f, t],
[f, f, f, f],
[f, f, f, f]]

and start = (3, 0) (bottom left) and end = (0, 0) (top left), 
the minimum number of steps required to reach the end is 7, 
since we would need to go through (1, 2) because there is a wall everywhere else on the second row. 
"""


def findShortestPath(board, start, end):
    minSteps = helper(board, start, end, 0)
    return minSteps if minSteps < float("inf") else None


def helper(board, cur, end, steps):
    y = cur[0]
    x = cur[1]
    # off the board
    if x < 0 or y < 0 or x >= len(board[0]) or y >= len(board):
        return float('inf')
    # doubled back
    if board[y][x] == None:
        return float("inf")
    # hit a wall
    if board[y][x] == True:
        return float("inf")
    # made it to the end
    if y == end[0] and x == end[1]:
        return steps
    board[y][x] = None

    minSteps = min(helper(board, [y, x + 1], end, steps + 1),
                   helper(board, [y, x - 1], end, steps + 1),
                   helper(board, [y + 1, x], end, steps + 1),
                   helper(board, [y - 1, x], end, steps + 1))
    board[y][x] = False
    return minSteps


board = [[False, False, False, False], [True, True, False, True],
         [False, False, False, False], [False, False, False, False]]

print(findShortestPath(board, [3, 0], [0, 0]))

# alternative approach:
# mark number of steps from origin on every cell. find the min value at the end
# O(n)