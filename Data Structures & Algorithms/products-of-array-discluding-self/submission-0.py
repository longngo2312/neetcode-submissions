class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        print("Initial result array: ", res)
        left = 1
        for i in range(len(nums)):
            print(f"iteration {i+1}")
            res[i] = left 
            print(f"original nums {nums}")
            print(f"updated array: {res}")
            left *= nums[i]
            print(f"updated left product: {left}")
        
        right = 1
        for i in range(len(nums) -1, -1, -1):
            print(f"iteration {i+1}")
            res[i] *= right 
            print(f"original nums {nums}")
            print(f"updated array: {res}")
            right *= nums[i]
            print(f"updated right product: {right}")
        print("final array: ", res)
        return res 