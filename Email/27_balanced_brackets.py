"""  
Given a string of round, curly, and square open and closing brackets, 
return whether the brackets are balanced (well-formed).

For example, given the string "([])[]({})", you should return true.

Given the string "([)]" or "((()", you should return false. 
"""


def balancedBrackets(str):
    openDict = {'(': True, '[': True, '{': True}
    closedDict = {')': '(', ']': '[', '}': '{'}
    openStack = []

    for char in str:
        if char in openDict:
            openStack.append(char)
        if char in closedDict:
            if openStack[-1] == closedDict[char]:
                openStack.pop()
            else:
                return False
    return len(openStack) == 0


assert balancedBrackets("([])[]({})") == True
assert balancedBrackets("([)]") == False
assert balancedBrackets("((()") == False