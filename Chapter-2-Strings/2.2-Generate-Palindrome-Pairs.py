""" 
Given a list of words, find all pairs of unique indices such that the concatenation of two words is a palindrome.

For example, given the list ['code', 'edoc', 'da', 'd'], return [(0,1), (1,0), (2,3)] 
"""

words = ["code", "edoc", "da", "d", "aa", "a"]

from collections import defaultdict


def isPalindrome(word):
    return word == word[::-1]


def generatePalindromePairs(wordsArr):
    result = []
    # create a dictionary of words and their indexes
    wordsDict = defaultdict(int)
    for i, word in enumerate(wordsArr):
        wordsDict[word] = i

    # cycle through each word
    for i, word in enumerate(wordsArr):
        for char_idx in range(len(word)):
            # split current word into prefix and suffix, split at the current char_idx
            prefix = word[:char_idx]
            suffix = word[char_idx:]

            prefixReversed = prefix[::-1]
            suffixReversed = suffix[::-1]

            if isPalindrome(suffix) and prefixReversed in wordsDict:
                if wordsDict[prefixReversed] != i:
                    result.append((i, wordsDict[prefixReversed]))

                    # edge case for when there are empty strings in the words array
                    if prefixReversed == "":
                        result.append([wordsDict[prefixReversed], i])
            if isPalindrome(prefix):
                if suffixReversed in wordsDict and wordsDict[
                        suffixReversed] != i:
                    result.append((wordsDict[suffixReversed], i))
    return result


print(generatePalindromePairs(words))
