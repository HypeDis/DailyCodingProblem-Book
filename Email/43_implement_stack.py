"""  
Implement a stack that has the following methods:

    push(val), which pushes an element onto the stack
    pop(), which pops off and returns the topmost element of the stack. If there are no elements in the stack, then it should throw an error or return null.
    max(), which returns the maximum value in the stack currently. If there are no elements in the stack, then it should throw an error or return null.

Each method should run in constant time. 
"""


class Stack:
    def __init__(self):
        self.maxes = []
        self.stack = []

    def push(self, num):
        self.stack.append(num)
        if not self.maxes or num >= self.maxes[-1]:
            self.maxes.append(num)
        return self

    def pop(self):
        if (not len(self.stack)):
            return None
        if self.stack[-1] == self.maxes[-1]:
            self.maxes.pop()
        self.stack.pop()

    def max(self):
        return self.maxes[-1]


myStack = Stack()

myStack.push(3).push(10).push(4).push(3)
assert myStack.max() == 10
myStack.push(11)
assert myStack.max() == 11
myStack.pop()
assert myStack.max() == 10
myStack.pop()
myStack.pop()
myStack.pop()
assert myStack.max() == 3
myStack.pop()
assert myStack.pop() == None