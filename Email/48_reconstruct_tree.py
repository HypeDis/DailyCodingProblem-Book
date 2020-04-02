"""
Good morning! Here's your coding interview problem for today.

This problem was asked by Google.

Given pre-order and in-order traversals of a binary tree, write a function to reconstruct the tree.

For example, given the following preorder traversal:

[a, b, d, e, c, f, g]

And the following inorder traversal:

[d, b, e, a, f, c, g]

You should return the following tree:

    a
   / \
  b   c
 / \ / \
d  e f  g
hi jk lm no
"""
'''

pre-order => root, left, right
[a, b, d, e, c, f, g]
'''

from collections import deque


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class RebuildTree:
    def __init__(self, traversalType):
        try:
            self.traversalType = traversalType
        except:
            raise Exception('please enter a traversal type')

    def buildTree(self, arr):
        if self.traversalType == 'pre':
            return self.preOrder(arr)
        elif self.traversalType == 'in':
            return self.inOrder(arr)

    def preOrder(self, arr):
        level = 0
        dist = len(arr) // 2

        root = Node(arr[0])
        queue = deque([{'node': root, 'idx': 0}])
        while queue:
            level += 1
            levelLen = len(queue)
            for i in range(levelLen):
                cur = queue.popleft()
                curNode = cur['node']
                left = cur['idx'] + 1
                right = left + dist
                leftNode = None
                rightNode = None
                if left < len(arr):
                    leftNode = Node(arr[left])
                    queue.append({'node': leftNode, 'idx': left})
                    curNode.left = leftNode
                if right < len(arr):
                    rightNode = Node(arr[right])
                    queue.append({'node': rightNode, 'idx': right})
                    curNode.right = rightNode
            dist = dist // 2
        return root

    def inOrder(self, arr):
        mid = len(arr) // 2
        dist = int((mid + 1) / 2)
        root = Node(arr[mid])
        queue = deque([{'node': root, 'idx': mid}])
        while queue:
            levelLen = len(queue)
            for i in range(levelLen):
                cur = queue.popleft()
                curNode = cur['node']
                curIdx = cur['idx']
                left = curIdx - dist
                right = curIdx + dist
                if left >= 0 and left != curIdx:
                    leftNode = Node(arr[left])
                    queue.append({'node': leftNode, 'idx': left})
                if right < len(arr) and right != curIdx:
                    rightNode = Node(arr[right])
                    queue.append({'node': rightNode, 'idx': right})
                curNode.left = leftNode
                curNode.right = rightNode
            dist = int(dist / 2)
            print('dist', dist)
        return root


preOrder = RebuildTree('pre')

preRoot = preOrder.buildTree(['a', 'b', 'd', 'e', 'c', 'f', 'g'])
print('***** pre order')
print(preRoot.val)
print(preRoot.left.val)
print(preRoot.right.val)
print(preRoot.left.left.val)
print(preRoot.left.right.val)
print(preRoot.right.left.val)
print(preRoot.right.right.val)

inOrder = RebuildTree('in')
inRoot = inOrder.buildTree(['d', 'b', 'e', 'a', 'f', 'c', 'g'])
print('******** in order')
print(inRoot.val)
print(inRoot.left.val)
print(inRoot.right.val)
print(inRoot.left.left.val)
print(inRoot.left.right.val)
print(inRoot.right.left.val)
print(inRoot.right.right.val)