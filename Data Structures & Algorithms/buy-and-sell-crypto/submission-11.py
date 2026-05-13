class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        res = 0
        for r in range(1, len(prices)):
            if prices[l] > prices[r]:
                l = r
                continue 
            else:
                diff = prices[r] - prices[l]
                res = max(res,diff)
        return res

