""" Given a linke list, alternate values so that they have a low, high, low, high... relationship. """

from classes import LinkedList

myList = LinkedList(1)
myList.insert(2).insert(3).insert(4).insert(5).insert(6)

print(myList.listNodes())


def rearrangeList(node, isLessThan):
    if node.next is None:
        return

    if (node.value > node.next.value
            and isLessThan) or (node.value < node.next.value
                                and not isLessThan):
        node.value, node.next.value = node.next.value, node.value

    rearrangeList(node.next, not isLessThan)


# rearrangeList(myList.head, True)

# print(myList.listNodes())


def bookSolution(li):
    prev = li.head
    curr = prev.next

    while curr:
        if prev.value > curr.value:
            prev.value, curr.value = curr.value, prev.value
        if not curr.next:
            break
        if curr.value < curr.next.value:
            curr.value, curr.next.value = curr.next.value, curr.value

        prev = curr.next
        curr = curr.next.next


bookSolution(myList)
print(myList.listNodes())