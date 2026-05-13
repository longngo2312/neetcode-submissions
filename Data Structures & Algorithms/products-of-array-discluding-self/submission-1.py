class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #initial result array
        res = [1] * len(nums)
        #left product set to 1
        left = 1
        #for every index in list 
        for num in range(len(nums)):
           #initialize the indexed value in result array to be equal to left 
            res[num] = left 
            #where left is equal to the product of left * the value in nums 
            left *= nums[num]
        right = 1
        #traverse the nums from right to left to find the product of all values on the right 
        #side of the nums and multiply those to the res value with the already product of all the value on the left except index 
        for i in range(len(nums)-1,-1,-1):
            res[i] *= right 
            right *= nums[i]
        return res 
        
