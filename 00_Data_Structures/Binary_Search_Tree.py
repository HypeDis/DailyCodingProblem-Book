class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Tree:
    def __init__(self, val=None):
        self.root = None
        if val:
            self.root = TreeNode(val)

    def insert(self, val):
        node = TreeNode(val)
        if not self.root:
            self.root = node
        else:
            self.insertHelper(self.root, node)

    def insertHelper(self, root, node):
        if not root.left and node.val < root.val:
            root.left = node
            return

        if not root.right and node.val > root.val:
            root.right = node
            return

        if node.val < root.val:
            self.insertHelper(root.left, node)
        else:
            self.insertHelper(root.right, node)
