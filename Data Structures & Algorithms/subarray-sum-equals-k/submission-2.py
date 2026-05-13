class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        currSum = 0
        PrefixSums = {0:1}
        for n in nums:
            currSum += n
            diff = currSum - k
            res += PrefixSums.get(diff,0)
            PrefixSums[currSum] = 1 + PrefixSums.get(currSum,0)
        return res