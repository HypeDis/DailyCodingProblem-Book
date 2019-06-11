""" 
The sequence [0,1,....N] has been jumbled, and the only clue you have for its order is an array representing whether each number is larger or smaller than the last. Given this information, reconstruct an array that is consistent with it. For example, given 
[None, + ,+, -, +], you could return [1,2,3,0,4] (there can be multiple solutions). 
"""

codedArray = [None, '+', '+', '-', '+']


# my solution
def myReconstruct(array):
    min = 0
    max = len(array) - 1

    answer = []

    for i in range(max):
        if array[i + 1] == '+':
            answer.append(min)
            min += 1
        else:
            answer.append(max)
            max -= 1
    answer.append(max)

    return answer


myReconstruct(codedArray)


# book solution
def solutionReconstruct(array):
    answer = []
    n = len(array) - 1
    stack = []

    for i in range(n):
        if array[i + 1] == '-':
            stack.append(i)
        else:
            answer.append(i)
            while stack:
                answer.append(stack.pop())
    answer.append(n)
    while stack:
        answer.append(stack.pop())

    return answer


solutionReconstruct(codedArray)