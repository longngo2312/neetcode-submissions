class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        res = []
        res += nums
        print(res)
        for num in nums: 
            res.append(num)
        return res