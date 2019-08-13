""" 
Given pre-order and in-order traversals of a binary tree, write a function to reconstruct the tree

 """
from TreeNode import Node
from Traverser import Traverser

a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
f = Node('f')
g = Node('g')

preOrder = [a, b, d, e, c, f, g]

inOrder = [d, b, e, a, f, c, g]


#  pre-order: root, left, right
def reconstruct(preOrder, inOrder):
    if not preOrder and not inOrder:
        return None
    if len(preOrder) == len(inOrder) == 1:
        return prekOrder[0]

    root = preOrder[0]
    inOrdRootIdx = inOrder.index(root)

    preLeft = preOrder[1:1 + inOrdRootIdx]
    inLeft = inOrder[0:inOrdRootIdx]

    preRight = preOrder[1 + inOrdRootIdx:]
    inRight = inOrder[inOrdRootIdx + 1:]

    root.left = reconstruct(preLeft, inLeft)
    root.right = reconstruct(preRight, inRight)

    return root


root = reconstruct(preOrder, inOrder)

traverser = Traverser()

print(traverser.preOrder(root))
print(traverser.inOrder(root))
