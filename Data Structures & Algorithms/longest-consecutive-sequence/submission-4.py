class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        setNum = set(nums)
        res = 0
        #iterate through array to check for sequence 
        for num in nums:
            #if nums[i] has a nums[i] - 1 value in set then it the start of sequcne
            if num - 1 not in setNum: #this mean num is the start 
                curr = 0
                while num + curr in setNum: #if the next number does exist (num+curr so that as length increases we will keep checking the next number)
                    curr += 1 #increment length
                res = max(res, curr)
        return res
        #TC: O(n) since we only loop through the array once so it depends on the length n of the arr
        #SC: O(n) had to use extra memory set to find left and right value
             
        