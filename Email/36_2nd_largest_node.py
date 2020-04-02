""" 
Given the root to a binary search tree, find the second largest node in the tree. 
"""

# largest value is right most node
# second largest value is either the largest values parent or
from heapq import *
import sys
sys.path.append(
    '/Users/markbae/Dropbox/Coding-Stuff/DailyCodingProblem/00_Data_Structures/'
)
from Binary_Search_Tree import Tree


def findSecondLargest(root):
    heap = helper(root, [])
    return heap[0]


def helper(root, heap):
    if not root:
        return heap
    heappush(heap, root.val)

    if len(heap) > 2:
        heappop(heap)
    helper(root.left, heap)
    helper(root.right, heap)
    return heap


tree = Tree(10)
tree.insert(12)
tree.insert(23)
tree.insert(13)
tree.insert(87)
tree.insert(45)
tree.insert(3)
tree.insert(93)
tree.insert(1)
tree.insert(77)
tree.insert(177)

print(findSecondLargest(tree.root))