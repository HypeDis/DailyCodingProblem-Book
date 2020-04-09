""" 
Given k sorted singly linked lists, 
write a function to merge all the lists into one sorted singly linked list. 
"""

from heapq import heappop, heappush
import sys
sys.path.append('00_Data_Structures')

from Singly_Linked_List import SinglyLinkedList


def mergeLists(lists):
    minHeap = []
    head = None
    curNode = None
    for list in lists:
        entry = (list.val, list)
        heappush(minHeap, entry)
    while minHeap:
        val, node = heappop(minHeap)
        if node.next:
            heappush(minHeap, (node.next.val, node.next))
        if not head:
            head = node
            curNode = head
        else:
            curNode.next = node
        node.next = None
        curNode = node
    return head


l1 = SinglyLinkedList()
l1.insert(3)
l1.insert(5)
l1.insert(6)
l1.insert(8)

l2 = SinglyLinkedList()
l2.insert(2)
l2.insert(7)
l2.insert(9)
l2.insert(12)

l3 = SinglyLinkedList()
l3.insert(1)
l3.insert(4)
l3.insert(10)
l3.insert(11)

mergedList = mergeLists([l1.head, l2.head, l3.head])
while mergedList:
    print(mergedList.val)
    mergedList = mergedList.next
