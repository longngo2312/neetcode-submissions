class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []
        currentCombination = [] 

        def backtracking(i, currentCombination):

            if len(currentCombination) == k: 
                result.append(currentCombination.copy())
                return 
            
            if i > n:
                return 
            

            #decision to add n 
            currentCombination.append(i)
            backtracking(i + 1, currentCombination)

            currentCombination.pop() 
            backtracking(i + 1, currentCombination)
        
        backtracking(1, currentCombination)
        return result
        