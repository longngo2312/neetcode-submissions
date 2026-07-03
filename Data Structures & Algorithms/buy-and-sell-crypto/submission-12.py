class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0 
        profit = 0 
        for right in range(1, len(prices)):
            if prices[left] > prices[right]:
                left += 1
            profit = max(profit, prices[right] - prices[left])

            while prices[left] > prices[right]:
                left += 1
        
        return profit