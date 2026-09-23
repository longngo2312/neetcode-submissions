class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = [] 
        currentSum = 0 
        subset = [] 
        def backtracking(start, currentSum, subset):
            if currentSum == target: 
                result.append(subset.copy())
                return 
            if currentSum > target: 
                return 
            
            for i in range(start, len(nums)):

                subset.append(nums[i])

                backtracking(i, currentSum + nums[i], subset) 
            

                subset.pop() 
        
        backtracking(0, currentSum, subset) 
        return result 