class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = [] 
        seen = defaultdict(bool)

        def backtrack(path): 
            if len(path) == len(nums): 
                res.append(path.copy()) 
                return 

            for i in range(len(nums)): 
                if not seen[nums[i]]:
                    path.append(nums[i])
                    seen[nums[i]] = True 
                    backtrack(path)

                    #clean up and backtrack to previous state to explore other options 
                    path.pop() 
                    seen[nums[i]] = False             
        backtrack([]) 
        return res