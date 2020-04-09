"""
Given a mapping of digits to letters (as in a phone number), and a digit string, return all possible letters the number could represent. 
You can assume each valid number in the mapping is a single digit.

For example if {“2”: [“a”, “b”, “c”], 3: [“d”, “e”, “f”], …} then “23” should return [“ad”, “ae”, “af”, “bd”, “be”, “bf”, “cd”, “ce”, “cf"]. 
"""
from collections import deque

digitMap = {
    2: ['a', 'b', 'c'],
    3: ['d', 'e', 'f'],
    4: ['g', 'h', 'i'],
    5: ['j', 'k', 'l'],
    6: ['m', 'n', 'o'],
    7: ['p', 'q', 'r', 's'],
    8: ['t', 'u', 'v'],
    9: ['w', 'x', 'y', 'z'],
}


def numberToWords(num):
    res = deque([''])
    while num:
        # working backwards from ones leftwards
        digit = num % 10
        num = num // 10
        queLen = len(res)
        for _ in range(queLen):
            curStr = res.popleft()
            for char in digitMap[digit]:
                res.append(char + curStr)

    return list(res)


print(numberToWords(253))
