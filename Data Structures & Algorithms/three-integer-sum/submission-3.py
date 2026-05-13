class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        print(nums)
        for index, value in enumerate(nums):
            if index > 0 and value == nums[index - 1]: #value == nums[index - 1] continue the loop if there's duplicate in value a 
                #index > 0 to make sure that it isn't the first value 
                continue 
            
            #init left and right pointers 
            l, r = index + 1, len(nums) - 1
            while l < r:
                threeSums = value + nums[l] + nums[r]
                print(threeSums, value, nums[r], nums[l])
                if threeSums > 0:
                    r -= 1
                elif threeSums < 0:
                    l += 1
                else:
                    res.append([value,nums[l],nums[r]])
                    l += 1 #doesn't have to decrement the r value since our sum will change accordingly thus r value will be decrement with the if statement
                    #this is to make sure there's no duplicates in our mini 2 sums problem 
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
        return res


