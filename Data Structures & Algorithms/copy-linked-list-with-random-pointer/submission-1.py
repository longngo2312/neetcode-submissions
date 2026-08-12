"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        oldToCopy = {None : None}

        #2 passes first pass to create the new nodes and build a hashmap 
        cur = head 
        while cur: 
            copy = Node(cur.val)
            oldToCopy[cur] = copy
            cur = cur.next
        
        #second pass to connect the pointers using our own hashmap 

        cur = head 
        while cur:
            copy = oldToCopy[cur]
            copy.next = oldToCopy[cur.next]
            copy.random = oldToCopy[cur.random]
            cur = cur.next 
        
        return oldToCopy[head]
