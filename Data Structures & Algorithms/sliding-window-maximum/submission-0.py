class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l = 0 
        r = k
        res = []
        while r <= len(nums):
            res.append(max(nums[l:r]))
            r += 1
            l += 1
        return res 