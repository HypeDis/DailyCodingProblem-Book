"""
Given a 2D matrix of characters and a target word, write a function that returns whether 
the word can be found in the matrix by going left-to-right, or up-to-down.

For example, given the following matrix:

[['F', 'A', 'C', 'I'],
 ['O', 'B', 'Q', 'P'],
 ['A', 'N', 'O', 'B'],
 ['M', 'A', 'S', 'S']]

and the target word 'FOAM', you should return true, since it's the leftmost column. 
Similarly, given the target word 'MASS', you should return true, since it's the last row. 
"""


def wordSearch(grid, word):
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            foundWord = checkDown(grid, x, y, word) or checkRight(
                grid, x, y, word)
            if foundWord:
                return True
    return False


def checkDown(grid, x, y, word):
    if not word:
        return True
    if y > len(grid) - 1:
        return False
    if word[0] != grid[y][x]:
        return False
    return checkDown(grid, x, y + 1, word[1:])


def checkRight(grid, x, y, word):
    if not word:
        return True
    if x > len(grid[0]) - 1:
        return False
    if word[0] != grid[y][x]:
        return False
    return checkRight(grid, x + 1, y, word[1:])


grid = [['F', 'A', 'C', 'I'], ['O', 'B', 'Q', 'P'], ['A', 'N', 'O', 'B'],
        ['M', 'A', 'S', 'S']]

print(wordSearch(grid, 'FOAM'))
print(wordSearch(grid, 'MASS'))