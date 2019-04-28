""" 
Given a string of round, curly, and square opening and closing brackets, return whether the brackets are balanced.

([])[]({}) returns true

([)) returns false

((() returns false 
"""

bracketPair = {")": "(", "}": "{", "]": "["}

# print(closingBrackets[")"])


def balancedBrackets(bracketStr):
    openBrackets = []

    for bracket in bracketStr:
        if bracket == "{" or bracket == "(" or bracket == "[":
            openBrackets.append(bracket)
        else:
            matchingBracket = bracketPair[bracket]
            if len(openBrackets) and openBrackets[len(openBrackets) -
                                                  1] == matchingBracket:
                openBrackets.pop()
            else:
                return False

    if (not len(openBrackets)):
        return True
    else:
        return False


print(balancedBrackets('([])[]({})'))
print(balancedBrackets('([))'))
print(balancedBrackets('((()'))
print(balancedBrackets('[()()]'))