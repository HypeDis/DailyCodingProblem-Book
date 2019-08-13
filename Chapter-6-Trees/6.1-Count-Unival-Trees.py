""" 
A unival tree (which stands for 'universal value') is a tree where all nodes under it have the same value.
given the root to a binary tree, count the number of unival subtrees
 """
from TreeNode import Node

# initialize tree
root = Node(0)
root.left = Node(1)
root.right = Node(0)

root.right.left = Node(1)
root.right.right = Node(0)

root.right.left.left = Node(1)
root.right.left.right = Node(1)


def countUnivals(root):
    count, _ = helper(root)
    print(count)


def helper(root):
    if root is None:
        return 0, True

    leftCount, isUnivalLeft = helper(root.left)
    rightCount, isUnivalRight = helper(root.right)

    count = leftCount + rightCount

    if isUnivalLeft and isUnivalRight:
        if root.left is not None and root.right.value != root.value:
            return count, False
        if root.right is not None and root.left.value != root.value:
            return count, False
        return count + 1, True
    return count, False


countUnivals(root)