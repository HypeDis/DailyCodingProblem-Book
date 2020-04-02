"""
There is an N by M matrix of zeroes. Given N and M, write a function to count the number of ways of starting at the top-left corner and getting to the bottom-right corner. You can only move right or down.

For example, given a 2 by 2 matrix, you should return 2, since there are two ways to get to the bottom-right:

    Right, then down
    Down, then right

Given a 5 by 5 matrix, there are 70 ways to get to the bottom-right. 
"""


def findWaysRecursive(m, n, curX, curY):
    if curY == m - 1 or curX == n - 1:
        return 1
    return findWaysRecursive(m, n, curX + 1, curY) + findWaysRecursive(
        m, n, curX, curY + 1)


def findWaysDp(m, n):
    dp = [[0] * n for _ in range(m)]
    for y in range(m):
        for x in range(n):
            if y - 1 < 0 or x - 1 < 0:
                dp[y][x] = 1
            else:
                dp[y][x] = dp[y - 1][x] + dp[y][x - 1]
    return dp[-1][-1]



print(findWaysRecursive(2, 2, 0, 0))
print(findWaysRecursive(5, 5, 0, 0))
print(findWaysDp(2, 2))
print(findWaysDp(5, 5))
