class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        subset = [] 
        result = [] 
        currentSum = 0 
        candidates.sort() 

        def backtracking(i, subset, currentSum):
            if currentSum == target: 
                result.append(subset.copy())
                return 
            
            if currentSum > target or i == len(candidates): 
                return 
            

            subset.append(candidates[i])
            backtracking(i + 1, subset, currentSum + candidates[i])
            subset.pop() 

            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1
            backtracking(i+1, subset, currentSum)
        
        backtracking(0, subset, currentSum)
        return result 