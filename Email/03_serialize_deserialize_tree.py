""" 
Given the root to a binary tree, implement serialize(root), 
which serializes the tree into a string, and deserialize(s), 
which deserializes the string back into the tree.
For example, given the following Node class

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

The following test should pass:

node = Node('root', Node('left', Node('left.left')), Node('right'))
assert deserialize(serialize(node)).left.left.val == 'left.left'
"""

from collections import deque


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def serialize(node):
    # run through nodes by BFS and add then to the string
    res = []
    separator = '@@'
    queue = deque([])
    queue.append(node)
    while queue:
        levelLength = len(queue)
        for i in range(levelLength):
            curNode = queue.popleft()
            if (curNode):
                # dont add a separator to the first element
                res.append((separator if res else '') + curNode.val)
            else:
                res.append(separator + 'None')
            if (curNode and curNode.left):
                queue.append(curNode.left)
            elif curNode:
                queue.append(None)
            if (curNode and curNode.right):
                queue.append(curNode.right)
            elif curNode:
                queue.append(None)
    return ''.join(res)


def deserialize(treeStr):
    treeVals = treeStr.split('@@')
    treeSize = len(treeVals) - 1
    #loop through the array and create nodes and add children to them
    for i in range(treeSize, -1, -1):
        curVal = treeVals[i]
        curNode = None
        if curVal == 'None':
            curNode = None
        else:
            curNode = Node(curVal)
        treeVals[i] = curNode

        leftI = i * 2 + 1
        rightI = i * 2 + 2
        if curNode:
            if leftI <= treeSize:
                curNode.left = treeVals[leftI]
            if rightI <= treeSize:
                curNode.right = treeVals[rightI]
    return treeVals[0]


node = Node('root', Node('left', Node('left.left')), Node('right'))
assert deserialize(serialize(node)).left.left.val == 'left.left'
