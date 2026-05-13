class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #bruteforce
        profit = 0 
        for i in range(len(prices)):
            for j in range(i+1, len(prices)):
                newProfit = prices[j] - prices[i]
                if newProfit > profit:
                    profit = newProfit 
        
        return profit 

    #TC: O(n^2)
    #SC: O(1)