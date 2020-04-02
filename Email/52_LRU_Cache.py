""" 
Implement an LRU (Least Recently Used) cache. It should be able to be initialized with a cache size n, and contain the following methods:

    set(key, value): sets key to value. If there are already n items in the cache and we are adding a new item, then it should also remove the least recently used item.
    get(key): gets the value at key. If no such key exists, return null.

Each operation should run in O(1) time. 
"""


class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


class LruCach:
    def __init__(self, size):
        self.size = size
        self.cache = {}
        self.head = Node('HEAD', None)
        self.tail = Node('TAIL', None)
        self.head.next = self.tail
        self.tail.prev = self.head

    def set(self, key, val):
        if key in self.cache:
            node = self.cache[key]
            node.val = val
            self.delete(node)
            self.insert(node)
        if key not in self.cache:
            newNode = Node(key, val)
            self.cache[key] = newNode
            self.insert(newNode)
            if len(self.cache) > self.size:
                lastNode = self.tail.prev
                self.delete(lastNode)
                self.cache.pop(lastNode.key)
        pass

    def get(self, key):
        if key in self.cache:
            curNode = self.cache[key]
            self.delete(curNode)
            self.insert(curNode)
            return curNode.val

        return None

    def insert(self, node):
        prevFirst = self.head.next
        self.head.next = node
        node.prev = self.head
        node.next = prevFirst
        prevFirst.prev = node

    def delete(self, node):
        prevNode = node.prev
        nextNode = node.next
        prevNode.next = nextNode
        nextNode.prev = prevNode


myLru = LruCach(5)

myLru.set('hello', 'world')
myLru.set('foo', 'bar')
myLru.set('baz', 'quq')
myLru.set('charlie', 'delta')
myLru.set('epsilon', 'frankie')
print(myLru.get('hello'))
print(vars(myLru.head.next))
myLru.set('india', 'julliet')
print(myLru.get('foo'))
myLru.set('charlie', 'day')
print(vars(myLru.head.next))
print(vars(myLru.head.next.next))
