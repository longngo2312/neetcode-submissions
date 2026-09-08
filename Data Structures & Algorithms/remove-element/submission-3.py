class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        res = 0

        l, r = 0, len(nums) - 1
        while l <= r:
            while r > 0 and nums[r] == val:
                r -= 1
            print("current l and current r:", l, r)
            if nums[l] == val and l < r:
                nums[l], nums[r] = nums[r], nums[l]
            l += 1
        
        for num in nums:
            if num != val:
                res += 1
        
        print(nums)
        return res

