from TreeNode import Node
""" 
               A
              / \
            B     C
           / \   / \
          D   E F   G
        / \  /     /
       H  I J     K
"""
# root
root = Node('A')

# level 1
root.left = Node('B')
root.right = Node('C')

# level 2
root.left.left = Node('D')
root.left.right = Node('E')

root.right.left = Node('F')
root.right.right = Node('G')

# level 3
root.left.left.left = Node('H')
root.left.left.right = Node('I')

root.left.right.left = Node('J')

root.right.right.left = Node('K')

# # root, left, right
# def preOrder(root, tree):
#     if not root:
#         return
#     tree.append(root.value)
#     preOrder(root.left, tree)
#     preOrder(root.right, tree)
#     return tree

# # left, root, right
# def inOrder(root, tree):
#     if not root:
#         return
#     inOrder(root.left, tree)
#     tree.append(root.value)
#     inOrder(root.right, tree)
#     return tree

# # left, right, root
# def postOrder(root, tree=[]):
#     if not root:
#         return
#     postOrder(root.left, tree)
#     postOrder(root.right, tree)
#     tree.append(root.value)
#     return tree


class Traverser:
    def __init__(self):
        return

    # def traverse(self, type, root):
    #     if type == 'preOrder':
    #         return self.preOrder(root)
    #     elif type == 'inOrder':
    #         return self.inOrder(root)
    #     elif type == 'postOrder':
    #         return self.postOrder(root)
    #     else:
    #         return

    def preOrder(self, root, tree=[]):
        if not root:
            return
        tree.append(root.value)
        self.preOrder(root.left, tree)
        self.preOrder(root.right, tree)
        return tree

    # left, root, right
    def inOrder(self, root, tree=[]):
        if not root:
            return
        self.inOrder(root.left, tree)
        tree.append(root.value)
        self.inOrder(root.right, tree)
        return tree

# left, right, root

    def postOrder(self, root, tree=[]):
        if not root:
            return
        self.postOrder(root.left, tree)
        self.postOrder(root.right, tree)
        tree.append(root.value)
        return tree


# treeTraverser(root, preOrder)
# treeTraverser(root, inOrder)
# treeTraverser(root, postOrder)
# print(preOrder(root))
# print(inOrder(root))
# print(postOrder(root))

# postOrder = Traverser('postOrder')
# print(postOrder.traverse(root))