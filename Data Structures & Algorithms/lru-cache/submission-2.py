class Node: 
    def __init__(self, key, value) -> None:
        self.key, self.value = key, value
        self.next = None 
        self.prev = None 
class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {} 
        self.cap = capacity
        self.left, self.right = Node(0,0), Node(0,0)
        self.left.next, self.right.prev = self.right, self.left


    def insertAfter(self, newNode):
        nxt, prev = self.right, self.right.prev 
        prev.next = newNode 
        newNode.next, newNode.prev = nxt, prev
        nxt.prev = newNode 

    def remove(self, node):
        nxt, prev = node.next, node.prev 
        prev.next = nxt 
        nxt.prev = prev 


    def get(self, key: int) -> int:
        if key in self.cache: 
            #swap Node(key) with MRU node 
            node = self.cache[key] 
            self.remove(node) 
            self.insertAfter(node)
            return node.value
        return -1 


    def put(self, key: int, value: int) -> None:
        if key in self.cache: 
            self.remove(self.cache[key])
        
        newNode = Node(key, value)
        self.cache[key] = newNode
        self.insertAfter(self.cache[key])
        if len(self.cache) > self.cap:
            LRU = self.left.next 
            self.remove(LRU)
            del self.cache[LRU.key]
