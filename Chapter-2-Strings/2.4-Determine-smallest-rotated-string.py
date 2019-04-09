""" 
You are given a string of length n and an integer k. The string can be manipulated by taking one of the first k letteres and moving it to the end of the string. 
Write a program to determine the lexicographically smallest string that can be created after an unlimited number of moves.  
"""


def smallestRotatedString(str, k):
    #   if k === 1 rotate and find smallest string
    # else string can be sorted
    if k == 1:
        minStr = str
        for i in range(len(str)):
            str = str[1::] + str[0]
            minStr = min(str, minStr)
        return minStr

    strArr = list(str)
    strArr.sort()
    return "".join(strArr)


print(smallestRotatedString("aabaa", 3))

