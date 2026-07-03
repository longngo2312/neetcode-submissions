'''
idea: Use two pointers on both ends of the input array. 
if heights at left is less than heights right increment left and vice versa 
to check for water contain we also need to declare the max Left and max Right variable 
the amount of water trapped is calc as maxLeft/maxRight - height at current shifted pointer
'''
class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        leftMax, rightMax = height[l], height[r]
        res = 0
        while l < r:
            if leftMax < rightMax:
                l += 1
                leftMax = max(leftMax, height[l])
                res += leftMax - height[l]
            else:
                r -= 1
                rightMax = max(rightMax, height[r])
                res += rightMax - height[r]

        return res
