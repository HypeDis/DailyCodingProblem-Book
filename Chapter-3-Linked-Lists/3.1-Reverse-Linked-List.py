from classes import LinkedList


myLinkedList = LinkedList(10)


def reverse(self):
    self.reverseNodes(None, self.head)


LinkedList.reverse = reverse


def reverseNodes(self, leftNode, midNode):
    # basecase reach end of list
    if not midNode.next:
        self.head = midNode
    else:
        self.reverseNodes(midNode, midNode.next)

    midNode.next = leftNode


LinkedList.reverseNodes = reverseNodes


def reverseNonRecursive(self):
    prev, current = None, self.head
    while current is not None:
        temp = current.next
        current.next = prev
        prev = current
        current = temp
    self.head = prev


LinkedList.reverseNonRecursive = reverseNonRecursive


myLinkedList.insert(20)
myLinkedList.insert(15)
myLinkedList.insert(91)
print(myLinkedList.listNodes())
myLinkedList.reverse()
print(myLinkedList.listNodes())
myLinkedList.reverseNonRecursive()
print(myLinkedList.listNodes())
myLinkedList.reverseNonRecursive()
print(myLinkedList.listNodes())
