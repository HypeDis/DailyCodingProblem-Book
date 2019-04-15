# each linked list is a number where the last digit is the head of the list
# ex: 123 would be 3 -> 2 -> 1
# Add two of these linked lists together.

from classes import LinkedList

# 99
list1 = LinkedList(1)
list1.insert(1)
# 25
list2 = LinkedList(5)
list2.insert(2)


# convert linked lists to integers and add them together
def addTwoLists(l1, l2):
    return getInteger(l1) + getInteger(l2)


# take an integer and create a linke list
def listFromInteger(num):
    newList = LinkedList(num % 10)
    num = num // 10
    while num is not 0:
        newList.insert(num % 10)
        num = num // 10

    return newList


def getInteger(myList):
    currentNode = myList.head
    currentPlace = 0
    integerVal = 0
    while currentNode:
        integerVal += currentNode.value * (10**currentPlace)
        currentPlace += 1
        currentNode = currentNode.next

    return integerVal


sum = addTwoLists(list1, list2)
print(listFromInteger(sum).listNodes())


# no helper functions
def sum2Lists(l1, l2):
    carry = 0
    # digits = []
    l1 = l1.head
    l2 = l2.head
    sumList = LinkedList()
    while l1 or l2:
        num1 = l1.value if l1 else 0
        num2 = l2.value if l2 else 0
        sumList.insert((num1 + num2 + carry) % 10)
        carry = (num1 + num2 + carry) // 10
        l1 = l1.next if l1.next else None
        l2 = l2.next if l2.next else None
    if carry:
        sumList.insert(carry)
    print(sumList.listNodes())


sum2Lists(list1, list2)