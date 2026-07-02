class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        sett = set()
        for i in range(len(nums)):
            hashMap = {}
            target = 0 - nums[i]
            for j in range(i + 1, len(nums)):
                difference = target - nums[j] 
                if difference in hashMap:
                    triplet = tuple(sorted([nums[i], nums[j], difference]))
                    if triplet not in sett:
                        sett.add(triplet)
                hashMap[nums[j]] = j
        
        for value in sett:
            res.append(list(value))

        return res 
