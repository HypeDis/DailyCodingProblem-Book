"""  
Given a string, find the longest palindromic contiguous substring. 
If there are more than one with the maximum length, return any one.

For example, the longest palindromic substring of "aabcdcb" is "bcdcb". 
The longest palindromic substring of "bananas" is "anana" 
"""


def longestPalindrome(str):
    res = ''
    for i in range(len(str)):
        palOdd = getPalindrome(str, i - 1, i + 1)
        palEven = ''
        if i < len(str) - 1 and str[i + 1] == str[i]:
            palEven = getPalindrome(str, i - 1, i + 2)
        if len(palOdd) > len(res) and len(palOdd) > len(palEven):
            res = palOdd
        elif len(palEven) > len(res) and len(palEven) > len(palOdd):
            res = palEven

    return res


def getPalindrome(str, left, right):
    if left < 0 or right > len(str) - 1 or str[left] != str[right]:
        return str[left + 1:right]

    return getPalindrome(str, left - 1, right + 1)


print(longestPalindrome('aabcdcb'))
print(longestPalindrome('bananas'))