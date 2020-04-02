""" Given the head of a singly linked list, reverse it in-place. """


class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


head = ListNode(1)
cur = head
for i in range(2, 11):
    cur.next = ListNode(i)
    cur = cur.next


def printList(head):
    list = []
    while head:
        list.append(head.val)
        head = head.next
    print(list)


# iterative solution
def reverseLLIterative(head):
    prev, cur, next = None, head, None
    while cur:
        next = cur.next
        cur.next = prev
        prev = cur
        cur = next
    return prev


# recursive solution
def revLLRecursive(head):
    if not head:
        return head
    if not head.next:
        return head
    newHead = revLLRecursive(head.next)
    prev = head.next
    prev.next = head
    head.next = None
    return newHead


printList(head)
newHead = reverseLLIterative(head)
printList(newHead)
reversedHead = revLLRecursive(newHead)
printList(reversedHead)
