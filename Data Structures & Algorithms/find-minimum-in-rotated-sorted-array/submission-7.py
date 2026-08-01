class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) -1
        leftMost = nums[0]
        rightMost = nums[-1]
        res = leftMost
        while l <= r:
            mid = (l + r) // 2
            res = min(res, nums[mid])
            if nums[mid] >= leftMost:
                l = mid + 1
            
            else:
                r = mid - 1

        return res 