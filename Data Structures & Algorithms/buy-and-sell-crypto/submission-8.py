class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #bruteforce
        # profit = 0 
        # for i in range(len(prices)):
        #     for j in range(i+1, len(prices)):
        #         newProfit = prices[j] - prices[i]
        #         if newProfit > profit:
        #             profit = newProfit 
        
        # return profit 

    #TC: O(n^2)
    #SC: O(1)

        #sliding window 
        l = 0
        r = 1 
        maxP = 0
        while r < len(prices):
            if prices[r] > prices[l]:
                newP = prices[r] - prices[l]
                maxP = max(maxP, newP)
            else:
                l = r 
            r += 1
        return maxP
        
