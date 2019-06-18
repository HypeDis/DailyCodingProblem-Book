""" 
Implement an LRU (least recently used) cache. The cache should be able to be initialized with cach size n, and provide the following methods: 
  
  set(key, value): set key to value . If there are already n items in the cache and we are adding a new item, also remove the least recently used item. 

  get(key): get the value at key. If no such key exists, return null
 """

# double linked list 
class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.head = None

class LinkedList: 
    def __init__(self):
        self.head = Node(None, 'head')
        self.tail = Node(None, 'tail')

        # initialize head and tail for ease of use
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def getHead(self):
        return self.head.next
    
    def getTail(self):
        return self.tail.prev
    
    # add a node to the end of the list
    def add(self, node):
        prev = self.getTail()
        next = prev.next
        prev.next = node
        node.prev = prev
        node.next = next
        next.prev = node
    
    # remove node from anywhere in the list
    def remove(self, node):
        prev = node.prev
        next = node.next
        prev.next = next
        next.prev = prev
    
    def print(self):
        curNode = self.getHead()
        myList = []
        while curNode.key:
            myList.append([curNode.key, curNode.val])
            curNode = curNode.next
        print (myList)

class LRU_Cache:
    def __init__(self, n):
        self.n = n
        self.dict = {}
        self.list = LinkedList()
    
    def set(self, key, val):
        # if key exists delete it from dict and from list
        if key in self.dict:
            oldNode = self.dict[key]
            self.list.remove(oldNode)
            del self.dict[key]
        # add new node to list and dict
        newNode = Node(key, val)
        self.dict[key] = newNode
        self.list.add(newNode)
        # if dict length is too long remove head from list and dict
        if len(self.dict) > self.n:
            head = self.list.getHead()
            self.list.remove(head)
            del self.dict[head.key]

    def get(self, key):
         if self.dict[key]:
             n = self.dict[key]
             #  move node to end of the list
             self.list.remove(n)
             self.list.add(n)
             return n.val

myCache = LRU_Cache(5)
myCache.set('hello', 'world')
myCache.set('foo', 'bar')
myCache.set('white', 'board')
myCache.list.print()
myCache.set('daily', 'coding')
myCache.list.print()
myCache.set('holly', 'wood')
myCache.list.print()
myCache.set('daily', 'driver')
myCache.list.print()
