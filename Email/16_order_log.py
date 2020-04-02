""" 
You run an e-commerce website and want to record the last N order ids in a log. 
Implement a data structure to accomplish this, with the following API:
    record(order_id): adds the order_id to the log
    get_last(i): gets the ith last element from the log. 
    i is guaranteed to be smaller than or equal to N.

You should be as efficient with time and space as possible. 
"""

# order logger uses a queue with a maximum size N

from collections import deque


class OrderLogger:
    def __init__(self, size):
        self.size = size
        self.log = deque([None for x in range(self.size)])

    def record(self, orderId):
        self.log.append(orderId)
        if len(self.log) > self.size:
            self.log.popleft()

    def getLast(self, i):
        if i < 1:
            errorMsg = "Value must be between 1 and {size}".format(
                size=self.size)
            raise (ValueError(errorMsg))

        idx = self.size - i
        return self.log[idx]


mylogger = OrderLogger(3)
mylogger.record(1)
mylogger.record(2)
mylogger.record(3)
mylogger.record(4)
print(mylogger.getLast(1))
print(mylogger.getLast(2))
print(mylogger.getLast(3))
print(mylogger.getLast(0))