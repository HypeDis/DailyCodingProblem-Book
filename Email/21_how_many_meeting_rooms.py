"""  
Given an array of time intervals (start, end) for classroom lectures (possibly overlapping), 
find the minimum number of rooms required.

For example, given [(30, 75), (0, 50), (60, 150)], you should return 2.
"""

from heapq import *
from typing import List


class Solution:
    def __init__(self):
        self.heap = []

    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        rooms = 0
        intervals.sort(key=lambda x: x[0])
        heappush(self.heap, intervals[0][1])
        for i in range(1, len(intervals)):
            if not self.heap or self.heap[0] > intervals[i][0]:
                rooms += 1
            if self.heap and self.heap[0] <= intervals[i][0]:
                heappop(self.heap)
            heappush(self.heap, intervals[i][1])
        return len(self.heap)


mySoln = Solution()
print(mySoln.minMeetingRooms([(30, 75), (0, 50), (60, 150)]))