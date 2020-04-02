""" 
Given an integer k and a string s, find the length of the longest substring 
that contains at most k distinct characters.

For example, given s = "abcba" and k = 2, 
the longest substring with k distinct characters is "bcb". 
"""


def findLongestSubstring(s, k):
    usedChars = {}
    maxLen = 0
    left = 0
    right = 0
    while right < len(s):
        char = s[right]
        if char not in usedChars:
            usedChars[char] = 0
        usedChars[char] += 1
        while len(usedChars) > k:
            delChar = s[left]
            usedChars[delChar] -= 1
            if (usedChars[delChar]) == 0:
                del usedChars[delChar]
            left += 1
        maxLen = max(maxLen, right - left + 1)
        right += 1

    return maxLen


print(findLongestSubstring('abcabb', 2))