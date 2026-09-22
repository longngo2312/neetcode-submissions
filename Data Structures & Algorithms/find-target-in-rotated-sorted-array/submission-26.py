class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        l, r = 0, len(nums) - 1 

        while l <= r: 
            m = (l + r) // 2
            if nums[m] == target: return m

            #left portion 

            if nums[m] >= nums[l]: 
                if target < nums[l] or target > nums[m]:
                    l = m + 1 #go right 

                else: 
                    r = m - 1
            #right portion 
            else: 
                if target > nums[r] or target < nums[m]:#go left 
                    r = m - 1
                else: 
                    l = m + 1
        return -1