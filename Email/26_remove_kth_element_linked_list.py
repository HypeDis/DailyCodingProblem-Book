"""  
Given a singly linked list and an integer k, remove the kth last element from the list. 
k is guaranteed to be smaller than the length of the list.

The list is very long, so making more than one pass is prohibitively expensive.

Do this in constant space and in one pass. 
"""


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class LinkedList:
    def __init__(self, val):
        self.head = Node(val)

    def insert(self, val):
        newNode = Node(val)
        curNode = self.head
        while curNode and curNode.next:
            curNode = curNode.next
        curNode.next = newNode

    def print(self):
        curNode = self.head
        while curNode:
            print(curNode.val)
            curNode = curNode.next


myLL = LinkedList(1)
myLL.insert(2)
myLL.insert(3)
myLL.insert(4)
myLL.insert(5)
myLL.insert(6)


def removeKthFromLastNode(head, n):
    fast = head
    slow = head
    # fast pointer should be n steps ahead of slow pointer because we want the
    # slow pointer to end at the position before the node that needs to be deleted
    # distance between last node and deleted node is n - 1
    for i in range(n):
        fast = fast.next

    # if we've gone past the last node we know that the first node must be deleted
    if not fast:
        return slow.next

    # now that the fast pointer is ahead, move both pointers in lockstep
    while fast.next:
        fast = fast.next
        slow = slow.next

    # remove the nth node from end (slow is pointing at the node before it)
    slow.next = slow.next.next
    return head
