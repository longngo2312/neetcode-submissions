class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # res = []
        # sett = set()
        # for i in range(len(nums)):
        #     hashMap = {}
        #     target = 0 - nums[i]
        #     for j in range(i + 1, len(nums)):
        #         difference = target - nums[j] 
        #         if difference in hashMap:
        #             triplet = tuple(sorted([nums[i], nums[j], difference]))
        #             if triplet not in sett:
        #                 sett.add(triplet)
        #         hashMap[nums[j]] = j
        
        # for value in sett:
        #     res.append(list(value))

        # return res 

        #optimized solution sorting input array and apply two pointers approach 
        nums.sort()
        res = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            l, r = i + 1, len(nums) - 1
            while l < r:
                threeSum = nums[i] + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0: 
                    l += 1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
        
        return res
