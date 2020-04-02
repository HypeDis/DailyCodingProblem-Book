"""  
Run-length encoding is a fast and simple method of encoding strings. 
The basic idea is to represent repeated successive characters as a single count and character. 
For example, the string "AAAABBBCCDAA" would be encoded as "4A3B2C1D2A".

Implement run-length encoding and decoding. You can assume the string to be 
encoded have no digits and consists solely of alphabetic characters. 
You can assume the string to be decoded is valid. 
"""


def encodeString(s):
    res = ''
    count = 0
    for i in range(len(s)):
        curChar = s[i]
        if i > 0 and curChar != s[i - 1]:
            res += str(count) + s[i - 1]
            count = 0
        count += 1
        if i == len(s) - 1:
            res += str(count) + curChar
    return res


def decodeStr(encodedStr):
    res = ''
    i = 0
    multiplier = ''
    while i < len(encodedStr):
        curChar = encodedStr[i]
        if curChar.isnumeric():
            multiplier += curChar
        else:
            res += curChar * int(multiplier)
            multiplier = ''
        i += 1
    return res


rawStr = "AAAABBBCCDAA"
encodedStr = "4A3B2C1D2A"

assert encodeString(rawStr) == encodedStr
assert decodeStr(encodedStr) == rawStr
