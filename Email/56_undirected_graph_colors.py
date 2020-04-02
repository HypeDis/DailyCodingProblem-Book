""" 
Given an undirected graph represented as an adjacency matrix and an integer k, 
write a function to determine whether each vertex in the graph can be colored such that no two adjacent vertices 
share the same color using at most k colors. 
"""

# undirected graphs are symmetrical about the y=x axis
# find the row with the most non zero indexes
# edge case, a node points to itself. no solution

adjMatrix = [
    [0, 1, 1, 1, 1],
    [1, 0, 1, 1, 0],
    [1, 1, 0, 0, 0],
    [1, 1, 0, 0, 1],
    [1, 0, 0, 1, 0],
]


def enoughColors(matrix, k):
    for row in matrix:
        adjacentNodes = row.count(1)
        if adjacentNodes + 1 > k:
            return False
    return True


print(enoughColors(adjMatrix, 4))
print(enoughColors(adjMatrix, 5))
