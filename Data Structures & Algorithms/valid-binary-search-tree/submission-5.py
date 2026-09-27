# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        leftMax = float("-infinity")
        rightMax = float("infinity")


        def dfs(node, leftMax, rightMax):
            if not node: 
                return True
            
            if node.val < rightMax and node.val > leftMax: 
                left = dfs(node.left, leftMax, node.val)
                right = dfs(node.right, node.val, rightMax)

                if left and right:
                    return True  

            return False 
        return dfs(root, leftMax, rightMax)