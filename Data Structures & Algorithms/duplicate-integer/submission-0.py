class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        print(seen)
        for num in nums:
            if num in seen:
                print(num)
                return True
            seen.add(num)
        return False 
            
