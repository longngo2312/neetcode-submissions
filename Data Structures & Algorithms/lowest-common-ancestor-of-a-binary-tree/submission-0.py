# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        count = 2  
        def dfs(node):
            nonlocal count
            if not node: 
                return None 
            
            if node is p or node is q: 
                count -= 1
                return node
            
            commonAncestor = node 
            left = dfs(node.left) 
            right = dfs(node.right) 

            if left and right: 
                return commonAncestor 
            
            return left if left else right 
        
        return dfs(root)