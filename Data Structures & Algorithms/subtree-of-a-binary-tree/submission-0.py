# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def sameTree(tree1, tree2):
            stack = [[tree1,tree2]]

            while stack: 
                tr1, tr2 = stack.pop() 

                if not tr1 and not tr2: 
                    continue 
                
                if not tr1 or not tr2 or tr1.val != tr2.val: 
                    return False 
                
                stack.append([tr1.left,tr2.left])
                stack.append([tr1.right,tr2.right])
            return True 
        
        def dfs(node) -> bool:
            if not node: 
                return False 
            
            if sameTree(node, subRoot):
                return True 
            left = dfs(node.left)
            right = dfs(node.right)

            return left or right
            
        return dfs(root)

