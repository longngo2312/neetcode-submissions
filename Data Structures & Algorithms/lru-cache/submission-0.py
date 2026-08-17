#doubly linked list to keep track of the LRU
class Node:
    def __init__(self, key, value) -> None:
        self.key, self.value = key, value 
        self.prev = None 
        self.next = None 
class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {} #hashmap for O(1) lookup 
        #left=LRU right=MRU linkedlist nodes (dummy nodes)
        self.left, self.right = Node(0,0), Node(0,0)
        self.left.next, self.right.prev = self.right, self.left
        self.cap = capacity #capacity of the cache  

    #helper function for remove and insert 
    def remove(self,node): #remove from cache 
        prev, nxt = node.prev, node.next 
        prev.next = nxt 
        nxt.prev = prev 
    def insert(self,node): #insert after 
        prev, nxt = self.right.prev, self.right 
        prev.next = node 
        node.next = nxt 
        node.prev = prev
        nxt.prev = node

    def get(self, key: int) -> int:
        if key in self.cache: 
            self.remove(self.cache[key]) #swap position of the node in the linkedlist according to the usage 
            self.insert(self.cache[key])
            return self.cache[key].value #save the pointer to the node in the hashmap 
        return -1 #-1 if key not exist 

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key]) #remove the node if key already exist so we can update it 
        newNode = Node(key,value)
        self.cache[key] = newNode
        self.insert(newNode)
        if len(self.cache) > self.cap:
            LRU = self.left.next 
            self.remove(LRU)
            del self.cache[LRU.key]
        

