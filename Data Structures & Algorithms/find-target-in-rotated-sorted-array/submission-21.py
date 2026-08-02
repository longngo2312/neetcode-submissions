class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            leftmost = nums[l] 
            rightmost = nums[r]
            mid = nums[m]
            if mid == target: 
                return m
            
            if mid >= leftmost:
                if target > mid: 
                    l = m + 1
                else:
                    if target < leftmost:
                        l = m + 1
                    else:
                        r = m - 1
            else:
                if target < mid:
                    r = m - 1 
                else:
                    if target > rightmost:
                        r = m - 1
                    else:
                        l = m + 1
        return -1 