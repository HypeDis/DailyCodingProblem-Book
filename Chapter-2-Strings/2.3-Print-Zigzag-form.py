""" 
Given a string and a number of lines k, print the string in zigzag form. In zigzag, characters are printed out diagonally from top left to bottom right until reaching the kth line, then back up to top right and so on. 
For example, given the sentence "thisisazigzag" and k = 4, you should print:
t     a      g
 h   s  z   a
  i i    i z 
   s      g   
   """


def printZigZag(str, k):
    currentRow = 0
    isDescending = True
    zigZagArr = []

    # create empty rows to store chars
    for _ in range(k):
        zigZagArr.append([])

    # loop through the string
    for char in str:
        # put the char in the correct row
        zigZagArr[currentRow].append(char)

        # add spaces to every other row
        for j in range(len(zigZagArr)):
            if j != currentRow:
                zigZagArr[j].append(" ")

        # increment or decrement the currentRow
        if isDescending:
            currentRow += 1
        else:
            currentRow -= 1

        #  switch directions
        if currentRow == k or currentRow == -1:
            currentRow = abs((abs(currentRow) - 2))
            isDescending = not isDescending
        # corner case when there is only 1 row
        if k == 1:
            currentRow = 0

    zigZagStr = ""
    for line in zigZagArr:
        zigZagStr += "".join(line) + "\n"

    return zigZagStr


print(printZigZag("thisisazigzag", 5))
