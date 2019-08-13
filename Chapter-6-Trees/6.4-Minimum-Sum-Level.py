# find the level with the smallest sum in a binary tree

import collections
deque = collections.deque
defaultdict = collections.defaultdict

from TreeNode import Node

root = Node(1)
root.left = Node(-10)
root.right = Node(5)
root.left.left = Node(-11)
root.left.right = Node(-1)
root.right.left = Node(4)
root.right.right = Node(15)


def find_smallest_level(root):
    level_sums = defaultdict(int)
    bft = deque([])
    bft.append((root, 0))
    while len(bft):
        node, level = bft.popleft()
        level_sums[level] += node.value
        if node.right:
            bft.append((node.right, level + 1))
        if node.left:
            bft.append((node.left, level + 1))
            #
    return min(level_sums, key=level_sums.get)


minVal = find_smallest_level(root)

print(minVal)
