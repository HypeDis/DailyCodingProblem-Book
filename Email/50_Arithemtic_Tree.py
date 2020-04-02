"""  
Suppose an arithmetic expression is given as a binary tree. Each leaf is an integer and each internal node is one of '+', '−', '∗', or '/'.

Given the root to such a tree, write a function to evaluate it.

For example, given the following tree:

    *
   / \
  +    +
 / \  / \
3  2  4  5

You should return 45, as it is (3 + 2) * (4 + 5). 
"""
"""  
if node is a number return it
if node is an operator do the operation of the return values and return it
"""


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


root = Node('*')
root.left = Node('+')
root.right = Node('+')
root.left.left = Node(3)
root.left.right = Node(2)
root.right.left = Node(4)
root.right.right = Node(5)


def calculateTree(root):
    if type(root.val) == int:
        return root.val

    if root.val == '+':
        return calculateTree(root.left) + calculateTree(root.right)
    if root.val == '-':
        return calculateTree(root.left) - calculateTree(root.right)
    if root.val == '*':
        return calculateTree(root.left) * calculateTree(root.right)
    if root.val == '/':
        return calculateTree(root.left) / calculateTree(root.right)


print(calculateTree(root))