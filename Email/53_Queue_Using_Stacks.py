""" 
Implement a queue using two stacks. Recall that a queue is a FIFO (first-in, first-out) 
data structure with the following methods: enqueue, which inserts an element into the queue, and dequeue, which removes it. 
"""
""" 
1,2,3,4

[1][]
[1][2]
[1][2,3]
dequeue => 1
[] [2,3] => 
[3,2][4]
dequeue => 2
[3][4] 
[3][4]
[3][4,5,6,7]
dequeue => 3
[][4,5,6,7] => [7,6,5,4][]

rules
1. if both are empty, put number in leftQ(start)
2. if leftQ is not empty put number in rightQ
3. always dequeue from leftQ
4. when leftQ is empty move all values from rightQ to leftQ
"""


class Queue:
    def __init__(self):
        self.leftQ = []
        self.rightQ = []

    def enqueue(self, val):
        if not self.leftQ:
            self.leftQ.append(val)
        else:
            self.rightQ.append(val)

    def dequeue(self):
        if not self.leftQ and not self.rightQ:
            return None
        if self.leftQ:
            return self.leftQ.pop()
        else:
            while self.rightQ:
                self.leftQ.append(self.rightQ.pop())
            return self.leftQ.pop()


myQueue = Queue()

myQueue.enqueue(1)
myQueue.enqueue(2)
myQueue.enqueue(3)
print(myQueue.dequeue())
