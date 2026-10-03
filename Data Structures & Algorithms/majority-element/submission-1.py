class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counter = Counter(nums)
        maxFrequency = 0
        res = 0
        print(counter)
        for key, value in counter.items():
            if value > maxFrequency: 
                res = key
                maxFrequency = value 
        return res 