""" 
Given two singly linked lists that intersect at some point k find the intersection nodes. Assume the lists are non-cyclical.

For example, given A = 3 -> 7 -> 8 -> 10 and B = 99 -> 1 -> 8 -> 10
return the node with value 8. In this example, assume nodes with the same value are the exact same node objects. 

Do this in O(m + n) time and constant space. 
"""

from classes import LinkedList

Alist = LinkedList(3).insert(7).insert(8).insert(10)
Blist = LinkedList(99).insert(1).insert(8).insert(10)

print(Alist.listNodes())
print(Blist.listNodes())


def findIntersection(l1, l2):
    l1 = l1.head
    l2 = l2.head

    l1Count = getLength(l1)
    l2Count = getLength(l2)

    biggerList = l1 if l1Count > l2Count else l2
    smallerList = l1 if biggerList == l2 else l2

    diff = abs(l1Count - l2Count)
    while diff:
        biggerList = biggerList.next
        diff -= 1
    while biggerList and smallerList:
        if biggerList.value == smallerList.value:
            return biggerList.value
        biggerList = biggerList.next
        smallerList = smallerList.next
    return None


def getLength(head):
    if not head:
        return 0
    return 1 + getLength(head.next)


print(findIntersection(Alist, Blist))


def bookSolution(a, b):
    m, n = getLength(a), getLength(b)
    cur_a, cur_b = a, b

    if m > n:
        for _ in range(m - n):
            cur_a = cur_a.next
    else:
        for _ in range(n - m):
            cur_b = cur_b.next
    while cur_a.value != cur_b.value:
        cur_a = cur_a.next
        cur_b = cur_b.next
    return cur_a.value


print(bookSolution(Alist.head, Blist.head))