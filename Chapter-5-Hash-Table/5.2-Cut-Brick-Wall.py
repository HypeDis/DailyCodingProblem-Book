"""
A wall consists of several rows of bricks of various integer lengths and uniform height. Your goal is to find a vertical line going from the top to the bottom of the wall that cuts through the fewest number of bricks. If the line goes through the edge between two bricks, this does not count as a cut.
 """

from collections import defaultdict
wall = [
    [3, 5, 1, 1],
    [2, 3, 3, 2],
    [5, 5],
    [4, 4, 2],
    [1, 3, 3, 3],
    [1, 1, 6, 1, 1]
]


def fewest_cuts(wall):
    cuts = defaultdict(int)

    for row in wall:
        length = 0
        for brick in row[:-1]:
            length += brick
            cuts[length] += 1

    maxLines = 0
    maxPosition = None
    for position in cuts:
        if cuts[position] > maxLines:
            maxLines = cuts[position]
            maxPosition = position

    totalRows = len(wall)
    print(
        f'the optimal position is {maxPosition}, with {totalRows - maxLines} cuts required')


fewest_cuts(wall)
