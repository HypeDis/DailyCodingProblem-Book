class Stack:
    def __init__(self):

        self.stack = []
        self.maxList = []

    def push(self, val):

        if not len(self.maxList) or val >= self.maxList[len(self.maxList) - 1]:
            self.maxList.append(val)

        self.stack.append(val)

    def pop(self):

        if (not len(self.stack)):
            raise Exception('stack is empty')

        popVal = self.stack.pop()

        if popVal == self.maxList[len(self.maxList) - 1]:
            self.maxList.pop()
        return popVal

    def max(self):
        if not len(self.stack):
            raise Exception('stack is empty')

        return self.maxList[len(self.maxList) - 1]


myStack = Stack()

# myStack.pop()
# myStack.max()
myStack.push(4)
myStack.push(10)
myStack.push(8)
myStack.push(7)
myStack.push(12)
print(myStack.stack)
print(myStack.max())
myStack.pop()
print(myStack.stack)
print(myStack.max())
print(myStack.maxList)