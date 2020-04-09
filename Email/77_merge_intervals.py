"""  
Given a list of possibly overlapping intervals, 
return a new list of intervals where all overlapping intervals have been merged.

The input list is not necessarily ordered in any way.

For example, given [(1, 3), (5, 8), (4, 10), (20, 25)], you should return [(1, 3), (4, 10), (20, 25)]. 
"""


def mergeIntervals(intervals):
    i = 0
    res = []
    curStart = None
    curEnd = None
    intervals.sort()
    while i < len(intervals):
        curInterval = intervals[i]
        if not curStart:
            curStart = curInterval[0]
            curEnd = curInterval[1]
        elif curInterval[0] > curEnd:
            res.append((curStart, curEnd))
            curStart, curEnd = curInterval[0], curInterval[1]
        else:
            curEnd = max(curEnd, curInterval[1])
        i += 1
        if i == len(intervals):
            res.append((curStart, curEnd))
    return res


i1 = [(1, 3), (5, 8), (4, 10), (20, 25)]
i2 = [(5, 8), (4, 10), (1, 3), (20, 25)]
i3 = [(1, 19)]
i4 = []
i5 = [(1, 2), (2, 4), (4, 8)]
assert mergeIntervals(i1) == [(1, 3), (4, 10), (20, 25)]
assert mergeIntervals(i2) == [(1, 3), (4, 10), (20, 25)]
assert mergeIntervals(i3) == [(1, 19)]
assert mergeIntervals(i4) == []
assert mergeIntervals(i5) == [(1, 8)]
print('all tests passed')
