# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        dummy = cur = ListNode()
        iteration = 0
        while l1 or l2:
            iteration += 1
            if l1:
                val1 = l1.val
            else:
                val1 = 0 
            
            if l2:
                val2 = l2.val 
            else:
                val2 = 0
            print("iteration: ", iteration)
            print("carry after: ", carry)
            value = val1 + val2 + carry
            carry = 0
            if value >= 10:
                carry = value // 10
                value = value % 10
            
            cur.next = ListNode(value)
            cur = cur.next 
            if l1 and l2:
                l1 = l1.next 
                l2 = l2.next 
            elif l1 and not l2:
                l1 = l1.next 
            else:
                l2 = l2.next 


        if carry > 0:
            cur.next = ListNode(carry)

        return dummy.next