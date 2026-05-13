class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        memory = [] #[value, index]
        #keep the memory of the index
        for i,val in enumerate(nums):
            memory.append([val,i])
        memory.sort()
        l = 0
        r = len(nums) - 1 
        res = []
        while l < r:
            summ = memory[l][0] + memory[r][0] 
            if summ == target:
                return [min(memory[l][1], memory[r][1]),max(memory[l][1],memory[r][1])]
            elif summ > target:
                r -= 1 
            else:
                l += 1
        print(res)
        return []



        