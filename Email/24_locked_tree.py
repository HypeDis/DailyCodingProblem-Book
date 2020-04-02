"""  
Implement locking in a binary tree. A binary tree node can be locked 
or unlocked only if all of its descendants OR ancestors are not locked.

Design a binary tree node class with the following methods:

    - is_locked, which returns whether the node is locked
    - lock, which attempts to lock the node. If it cannot be locked, 
    then it should return false. Otherwise, it should lock it and return true.
    - unlock, which unlocks the node. If it cannot be unlocked, 
    then it should return false. Otherwise, it should unlock it and return true.

You may augment the node to add parent pointers or any other property you would like. 
You may assume the class is used in a single-threaded program, 
so there is no need for actual locks or mutexes. Each method should run in O(h), 
where h is the height of the tree. 
"""


class Node:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.left = None
        self.right = None
        self.isLocked = False
        self.lockedChildren = 0


class LockedTree:
    def __init__(self, val):
        self.root = Node(val)

    def insert(self, val):
        newNode = Node(val)
        curNode = self.root
        while (curNode):
            if not curNode.left and val < curNode.val:
                curNode.left = newNode
                newNode.prev = curNode
                return newNode

            if not curNode.right and val > curNode.val:
                curNode.right = newNode
                newNode.prev = curNode
                return newNode

            if val < curNode.val:
                curNode = curNode.left
            else:
                curNode = curNode.right

    def isLocked(self, node):
        return node.isLocked

    def lock(self, node):
        if (node.isLocked):
            return True
        if (self.canChangeStatus(node)):
            node.isLocked = True
            self.incrementLockedChildren(node)
            return True
        else:
            return False

    def unlock(self, node):
        if not node.isLocked:
            return True
        if (self.canChangeStatus(node)):
            node.isLocked = False
            self.decrementLockedChildren(node)
            return True
        else:
            return False

    def canChangeStatus(self, node):
        if node.lockedChildren > 0:
            return False
        while node.prev:
            node = node.prev
            if node.isLocked:
                return False
        return True

    def decrementLockedChildren(self, node):
        while (node.prev):
            node = node.prev
            node.lockedChildren -= 1

    def incrementLockedChildren(self, node):
        while (node.prev):
            node = node.prev
            node.lockedChildren += 1


lTree = LockedTree(10)
n1 = lTree.root
n2 = lTree.insert(15)
n3 = lTree.insert(5)
n4 = lTree.insert(30)
n5 = lTree.insert(20)
n6 = lTree.insert(3)
n7 = lTree.insert(8)

print(lTree.lock(n7))  # True
print(lTree.lock(n4))  # True
print(lTree.lock(n1))  # False
print(lTree.unlock(n7))  # True
print(lTree.lock(n6))  #True
print(lTree.lock(n3))  # False
print(lTree.unlock(n6))  # True
print(lTree.lock(n3))  # True
