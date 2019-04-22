class LinkedList:
    def __init__(self, val=None):
        if not val:
            self.head = None
        else:
            self.head = Node(val)

    def insert(self, val):
        if self.head == None:
            self.head = Node(val)
        else:
            self.insertNode(self.head, Node(val))
        return self

    def insertNode(self, midNode, newNode):
        if not midNode.next:
            midNode.next = newNode
        else:
            self.insertNode(midNode.next, newNode)

    def listNodes(self):
        nodes = []
        midNode = self.head
        while midNode:
            nodes.append(midNode.value)
            midNode = midNode.next
        return nodes


class Node:
    def __init__(self, val):
        self.value = val
        self.next = None
