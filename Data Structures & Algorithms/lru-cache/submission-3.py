class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        #2 pointers for previous and next nodes
        self.prev, self.next = None, None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {} #Map key to nodes

        #Have dummy nodes
        #Left is LRU, Right is MRU
        self.left, self.right = Node(0,0), Node(0,0)
        #Connect these nodes
        self.left.next, self.right.prev = self.right, self.left
        
    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next = nxt
        nxt.prev = prev

    def insert(self, node):
        prev, nxt = self.right.prev, self.right
        prev.next, nxt.prev = node, node
        node.next = nxt
        node.prev = prev

    def get(self, key: int) -> int:
        if key in self.cache:
            #Reorder and return value
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        #If key is there, remove it
        if key in self.cache:
            self.remove(self.cache[key])
        
        # Insert the new value
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        # If the length exceed 
        if len(self.cache) > self.capacity:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]