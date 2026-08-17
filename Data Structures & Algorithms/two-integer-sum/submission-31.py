class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #brute force O(n^2) problem 2 loops if they added up to target return 
        for i in range(len(nums)):
            for j in range(1, len(nums)):
                if nums[i] + nums[j] == target and i != j:
                    return [i,j]
        return []