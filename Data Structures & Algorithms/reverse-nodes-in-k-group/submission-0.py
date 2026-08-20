# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        arr = []
        curr = head 
        while curr: 
            arr.append(curr.val)
            curr = curr.next 

        l = 0
        while l <= len(arr):
            temp = r = l + k - 1
            while l <= r and r < len(arr):
                arr[l], arr[r] = arr[r], arr[l]
                l += 1 
                r -= 1
            l = temp + 1
        dummy = curr = ListNode()
        for num in arr:
            newNode = ListNode(num)
            curr.next = newNode 
            curr = curr.next 
        
        return dummy.next 