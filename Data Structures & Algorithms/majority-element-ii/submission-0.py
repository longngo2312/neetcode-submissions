class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        counter = Counter(nums)
        value = len(nums) / 3
        res = [] 
        for key, val in counter.items():
            if val > value:
                res.append(key)

        return res