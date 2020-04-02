'''
Given two singly linked lists that intersect at some point, 
find the intersecting node. The lists are non-cyclical.

For example, given A = 3 -> 7 -> 8 -> 10 and B = 99 -> 1 -> 8 -> 10, 
return the node with value 8.

In this example, assume nodes with the same value are the exact same node objects.

Do this in O(M + N) time (where M and N are the lengths of the lists) and constant space
'''
import sys
sys.path.append(
    '/Users/markbae/Dropbox/Coding-Stuff/DailyCodingProblem/00_Data_Structures/'
)
from Singly_Linked_List import SinglyLinkedList
'''
12 -> 3 -> 7 -> 8 -> 10
99 -> 1 -> 8 -> 10
'''
list1 = SinglyLinkedList()
list1.insert(12).insert(3).insert(7).insert(8).insert(10)

list2 = SinglyLinkedList()
list2.insert(99).insert(1).insert(8).insert(10)


def findIntersection(l1, l2):
    l1Dict = {}
    while l1:
        l1Dict[l1.val] = True
        l1 = l1.next
    while l2:
        if l2.val in l1Dict:
            return l2.val
        l2 = l2.next
    return None


print(findIntersection(list1.head, list2.head))

# using a hashtable here so its not constant space
# to do it in constant space I would add another key to each node called "visited". This would also require that I
# have the nodes actually be the same instead of faking it by having the same values

# another method would be O(m + n + n) where I traverse both lists to get their length
# and find the offset then traverse them together until the nodes are equal to each other
