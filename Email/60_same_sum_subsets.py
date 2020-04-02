"""
Given a multiset of integers, return whether it can be partitioned into two subsets whose sums are the same.

For example, given the multiset {15, 5, 20, 10, 35, 15, 10}, it would return true, 
since we can split it up into {15, 5, 10, 15, 10} and {20, 35}, which both add up to 55.

Given the multiset {15, 5, 20, 10, 35}, it would return false, since we can't split it up into two subsets that add up to the same sum. 
"""


def canPartition(mset):
    if not mset:
        return True
    if sum(mset) % 2 == 1:
        return False

    return helper(mset, 0, len(mset) - 1, 0, sum(mset))


def helper(mset, start, end, sum1, sum2):
    if start >= end:
        return False
    if sum1 == sum2:
        return True
    mset.sort()
    return helper(mset, start + 1, end,
                  sum1 + mset[start], sum2 - mset[start]) or helper(
                      mset, start, end - 1, sum1 + mset[end], sum2 - mset[end])


print(canPartition([15, 5, 20, 10, 35, 15, 10]))
print(canPartition([15, 5, 20, 10, 35]))