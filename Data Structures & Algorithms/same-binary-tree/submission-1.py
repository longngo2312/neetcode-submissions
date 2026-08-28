# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        stack = [[p,q]]

        while stack: 
            tr1, tr2 = stack.pop() 

            if not tr1 and not tr2: 
                continue 
            
            if not tr1 or not tr2 or tr1.val != tr2.val: 
                return False 
            
            stack.append([tr1.left,tr2.left])
            stack.append([tr1.right,tr2.right])
        return True 