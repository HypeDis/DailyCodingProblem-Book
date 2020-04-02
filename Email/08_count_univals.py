""" 
A unival tree (which stands for "universal value") is a tree where 
all nodes under it have the same value.

Given the root to a binary tree, count the number of unival subtrees.

For example, the following tree has 5 unival subtrees 
"""


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


root = TreeNode(1)
root.left = TreeNode(0)
root.right = TreeNode(0)


def countUnivals(root):
    return helper(root)[0]


def helper(self, root):
    if not root:
        return 0, True

    if not root.left and not root.right:
        return 1, True

    lCount, lIsUnival = self.helper(root.left)
    rCount, rIsUnival = self.helper(root.right)

    if lIsUnival and rIsUnival and (root.right is None
                                    or root.right.val == root.val) and (
                                        root.left is None
                                        or root.left.val == root.val):
        return lCount + rCount + 1, True
    else:
        return lCount + rCount, False


print(countUnivals(root))
