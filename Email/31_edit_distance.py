"""  
The edit distance between two strings refers to the minimum number of 
character insertions, deletions, and substitutions required to change 
one string to the other. For example, the edit distance between “kitten” 
and “sitting” is three: substitute the “k” for “s”, substitute the “e” for “i”, 
and append a “g”.

Given two strings, compute the edit distance between them. 
"""


# transform string 1 to string 2
def getEditDist(str1, str2):
    if not str1 or not str2:
        return len(str1) if str1 else len(str2)

    # initialize matrix
    matrix = [[0] * (len(str1) + 1) for n in range(len(str2) + 1)]
    for i in range(len(matrix[0])):
        matrix[0][i] = i
    for i in range(len(matrix)):
        matrix[i][0] = i
    print(matrix)

    for row in range(1, len(matrix)):
        for col in range(1, len(matrix[0])):
            char1, char2 = str1[col - 1], str2[row - 1]
            if char1 == char2:
                matrix[row][col] = matrix[row - 1][col - 1]
            else:
                matrix[row][col] = min(matrix[row][col - 1],
                                       matrix[row - 1][col],
                                       matrix[row - 1][col - 1]) + 1

    # for i in range(len(matrix)):
    #     print(matrix[i])

    return matrix[-1][-1]


# str1 = 'holy'
# str2 = 'hell'
# assert getEditDist(str1, str2) == 2

str3 = 'abc'
str4 = 'abcdef'
str5 = 'adbefc'

assert getEditDist(str3, str4) == 3
assert getEditDist(str4, str3) == 3
assert getEditDist(str3, str5) == 3
assert getEditDist(str4, str5) == 4
