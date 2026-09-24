class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []
        currentCombination = [] 

        def backtracking(start, currentCombination):

            if len(currentCombination) == k: 
                result.append(currentCombination.copy())
                return 
            #decision to add n 
            for i in range(start, n + 1):
                currentCombination.append(i)
                backtracking(i + 1, currentCombination)
                currentCombination.pop()

        backtracking(1, currentCombination)
        return result
        