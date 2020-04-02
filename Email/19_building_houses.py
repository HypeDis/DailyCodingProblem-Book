""" 
A builder is looking to build a row of N houses that can be of K different colors. 
He has a goal of minimizing cost while ensuring that 
no two neighboring houses are of the same color.

Given an N by K matrix where the nth row and kth column represents the 
cost to build the nth house with kth color, return the minimum cost which achieves this goal. 
"""
"""
        color
house   [ 2,1,3]
        [ 1,2,3]
        [ 3,2,1]
    
"""


# recursive solution O(n^n) very slow
def findMinCost(matrix):
    return helper(0, 0, -1, matrix)


def helper(cost, curLevel, prevK, matrix):
    res = []
    k = len(matrix[0])
    for i in range(k):
        if i is not prevK:
            curHouse = matrix[curLevel][i]
            if curLevel < len(matrix) - 1:
                res.append(helper(cost + curHouse, curLevel + 1, i, matrix))
            else:
                res.append(cost + matrix[curLevel][i])

    return min(res)


# print(findMinCost([
#     [2, 1, 3],
#     [1, 2, 3],
#     [3, 2, 1],
# ]))

# print(
#     findMinCost([[7, 3, 8, 6, 1, 2], [5, 6, 7, 2, 4, 3], [10, 1, 4, 9, 7, 6],
#                  [10, 1, 4, 9, 7, 6]]))


# O(n) time and space complexity
def findMinCostDP(costs):
    if not costs:
        return None

    n = len(costs)
    k = len(costs[0])

    # create an empty matrix that is the same size as the input
    minCosts = [[None] * k for _ in range(n)]
    # preload the first row
    minCosts[0] = costs[0]
    # prevMin and prevSecondMin will be the minimum values of the previous rows sums
    prevMin = None
    prevSecondMin = None
    # find the min and second min for 1st row
    for i in range(k):
        if not prevSecondMin or costs[0][i] < prevSecondMin:
            prevSecondMin = costs[0][i]
        if not prevMin or prevSecondMin < prevMin:
            prevMin, prevSecondMin = prevSecondMin, prevMin
    # start iterating from the 2nd row
    for row in range(1, n):
        curMin = None
        curSecondMin = None
        prevRow = minCosts[row - 1]
        for col in range(k):
            curHouseCost = costs[row][col]
            # if prevMin is on the same column as current column return the second min
            prevSum = (prevMin if prevRow[col] != prevMin else prevSecondMin)
            curSum = curHouseCost + prevSum
            minCosts[row][col] = curSum

            if not curSecondMin or curSum < curSecondMin:
                curSecondMin = curSum
            if not curMin or curSecondMin < curMin:
                curMin, curSecondMin = curSecondMin, curMin
        prevMin = curMin
        prevSecondMin = curSecondMin

    return min(minCosts[-1])


costs = [
    [1, 2, 2, 2, 2, 2],
    [1, 4, 3, 3, 5, 2],
    [1, 2, 2, 2, 2, 2],
    [2, 2, 1, 2, 2, 2],
    [1, 2, 2, 2, 2, 2],
]
print(findMinCostDP(costs))
