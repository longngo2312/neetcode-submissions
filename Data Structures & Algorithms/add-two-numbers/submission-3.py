# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        dummy = cur = ListNode()

        while l1 or l2:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            value = val1 + val2 + carry
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