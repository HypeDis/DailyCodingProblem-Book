""" 
Given the root of a binary tree, return a deepest node. For example, in the following tree, return d.

    a
   / \
  b   c
 /
d
"""


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def findDeepest(root):
    depth, root = helper(root)
    return root.val


def helper(root):
    if not root:
        return (0, None)
    if not root.left and not root.right:
        return (1, root)

    left = helper(root.left)
    right = helper(root.right)

    depth, root = max(left, right)
    return (1 + depth, root)




root = TreeNode('a')
root.left = TreeNode('b')
root.right = TreeNode('c')
root.left.left = TreeNode('d')

assert findDeepest(root) == 'd'
print('all tests passed')