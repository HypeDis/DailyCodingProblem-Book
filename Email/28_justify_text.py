"""  
Write an algorithm to justify text. Given a sequence of words and an integer line length k, 
return a list of strings which represents each line, fully justified.

More specifically, you should have as many words as possible in each line. 
There should be at least one space between each word. Pad extra spaces when necessary 
so that each line has exactly length k. Spaces should be distributed as equally as possible, with the extra spaces, 
if any, distributed starting from the left.

If you can only fit one word on a line, then you should pad the right-hand side with spaces.

Each word is guaranteed not to be longer than k.

For example, given the list of words 
["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"] 
and k = 16, you should return the following:

["the  quick brown", # 1 extra space on the left
"fox  jumps  over", # 2 extra spaces distributed evenly
"the   lazy   dog"] # 4 extra spaces distributed evenly
"""


def justify(list, k):
    rows = []
    i = 0
    curRow = []
    charCount = 0
    spaces = 0
    while i <= len(list):
        word = list[i] if i < len(list) else ''
        if i < len(list) and len(word) + charCount + spaces < k:
            curRow.append(word)
            charCount += len(word)
            spaces += 1
            i += 1
        else:
            gaps = len(curRow) - 1
            totalSpaces = k - charCount
            spacesPerWord = totalSpaces // gaps
            extraspaces = totalSpaces % gaps
            spacesArr = [' ' * spacesPerWord] * gaps
            j = 0
            while extraspaces > 0:
                print('while ', j)
                spacesArr[j] += ' '
                extraspaces -= 1
                j += 1
            rowStr = ''
            for l, word in enumerate(curRow):
                rowStr += word
                if l < len(spacesArr):
                    rowStr += spacesArr[l]
            rows.append(rowStr)
            curRow = []
            charCount = 0
            spaces = 0
            if i == len(list):
                break
    return rows


print(
    justify([
        "the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"
    ], 16))
