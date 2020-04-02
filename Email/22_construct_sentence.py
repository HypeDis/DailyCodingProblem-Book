"""  
Given a dictionary of words and a string made up of those words (no spaces), 
return the original sentence in a list. If there is more than one possible reconstruction, 
return any of them. If there is no possible reconstruction, then return null.

For example, given the set of words 'quick', 'brown', 'the', 'fox', and the string "thequickbrownfox", 
you should return ['the', 'quick', 'brown', 'fox'].

Given the set of words 'bed', 'bath', 'bedbath', 'and', 'beyond', 
and the string "bedbathandbeyond", return either ['bed', 'bath', 'and', 'beyond] or ['bedbath', 'and', 'beyond']. 
"""


def constructSentences(words, str):
    wordDict = {word: True for word in words}
    res = []

    left, right = 0, 0
    curWord = ''
    while right < len(str):
        curWord += str[right]
        if curWord in wordDict:
            res.append(curWord)
            right += 1
            left = right
            curWord = ''
        else:
            right += 1
    return None if curWord else res


str = "bedbathandbeyond"
words = [
    'bed',
    'bath',
    'bedbath',
    'and',
    'beyond',
]

print(constructSentences(words, str))
