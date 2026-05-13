class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums)
        l = 0
        r = len(nums) - 1 
        i = len(nums) - 1
        while l <= r:
            squaredL = nums[l]**2
            squaredR = nums[r]**2
            if squaredR > squaredL:
                res[i] = squaredR
                r -= 1
            else:
                res[i] = squaredL
                l += 1
            i -= 1
        return res
        #TC: O(n)
        #SC: O(1)