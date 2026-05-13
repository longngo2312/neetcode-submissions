class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        sett = set()
        for i in range(len(nums)):
            if nums[i] in sett:
                return True
            else:
                sett.add(nums[i])
        return False 