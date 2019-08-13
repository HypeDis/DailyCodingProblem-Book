""" 
Suppose an arithmetic expression is given as a binary tree. Each leaf is an integer and each internal node is one of +,-,*,or /.
Given the root to such a tree, write a function to evaluate it.
For example, given the following tree:

         *
        / \ 
       +   +
      /\   /\
     3  2 4  5
 """
from TreeNode import Node

"create an array of in-order traversal"

root = Node('*')
root.left = Node('+')
root.right = Node('+')
root.left.left = Node(3)
root.left.right = Node(2)
root.right.left = Node(4)
root.right.right = Node(5)

PLUS = '+'
MINUS = '-'
TIMES = '*'
DIVIDE = '/'


def evaluate(root):
    if root.value == PLUS:
        return evaluate(root.left) + evaluate(root.right)
    elif root.value == MINUS:
        return evaluate(root.left) - evaluate(root.right)
    elif root.value == TIMES:
        return evaluate(root.left) * evaluate(root.right)
    elif root.value == DIVIDE:
        return evaluate(root.left) / evaluate(root.right)
    else:
        return root.value


print(evaluate(root))