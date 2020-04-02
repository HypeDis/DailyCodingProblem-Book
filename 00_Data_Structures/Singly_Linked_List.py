class Node:
    def __init__(self, val):
        if not val:
            raise (ValueError('Value can not be empty'))
        self.val = val
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert(self, val):
        newNode = Node(val)
        if not self.head:
            self.head = newNode
        else:
            curNode = self.head
            while curNode.next:
                curNode = curNode.next
            curNode.next = newNode
        return self