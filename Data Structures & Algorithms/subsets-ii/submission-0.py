class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        subsets, curSet = [], [] 
        nums.sort() #O(nlogn)
        def dfs(i, nums, subsets, curSet):
            if i >= len(nums):
                subsets.append(curSet.copy())
                return 
            

            #decision to include nums[i] 
            curSet.append(nums[i])
            dfs(i + 1, nums, subsets, curSet)
            curSet.pop() #clearing for the backtrack into the other decision 

            #decision not to include nums[i] 

            #we need to skip duplicates value first  
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            dfs(i + 1, nums, subsets, curSet)
        
        dfs(0, nums, subsets, curSet)
        return subsets