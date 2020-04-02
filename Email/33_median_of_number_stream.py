"""  
Compute the running median of a sequence of numbers. 
That is, given a stream of numbers, print out the median of the list so far on each new element.

Recall that the median of an even-numbered list is the average of the two middle numbers.

For example, given the sequence [2, 1, 5, 7, 2, 0, 5], your algorithm should print out:

2
1.5
2
3.5
2
2
2
"""

from heapq import *


class MedianFinder:
    def __init__(self):
        # store the extra value in the right heap
        self.leftHeap = []  # numbers less than the median
        self.rightHeap = []  # numbers greater than or equal to the median

    def insert(self, val):
        # if type(val) != int or type(val) != float:
        #     raise ValueError('value must be a number')

        if not self.rightHeap or self.rightHeap[0] <= val:
            heappush(self.rightHeap, val)
        elif not self.leftHeap or val <= -self.leftHeap[0]:
            heappush(self.leftHeap, -val)
        self.rebalance()

    def rebalance(self):
        if len(self.leftHeap) > len(self.rightHeap):
            heappush(self.rightHeap, -heappop(self.leftHeap))
        if len(self.rightHeap) > len(self.leftHeap) + 1:
            heappush(self.leftHeap, -heappop(self.rightHeap))

    def getMedian(self):
        if len(self.rightHeap) == len(self.leftHeap):
            return (-self.leftHeap[0] + self.rightHeap[0]) / 2
        else:
            return self.rightHeap[0]


myMF = MedianFinder()

nums = [2, 1, 5, 7, 2, 0, 5]
medians = [2, 1.5, 2, 3.5, 2, 2, 2]
for i, num in enumerate(nums):
    myMF.insert(num)
    assert myMF.getMedian() == medians[i]