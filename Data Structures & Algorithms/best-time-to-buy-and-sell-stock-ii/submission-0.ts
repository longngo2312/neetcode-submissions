class Solution {
    /**
     * @param {number[]} prices
     * @return {number}
     */
    maxProfit(prices: number[]): number {
        if (!prices || prices.length < 2){
            return 0;
        }

        let maxProfit: number = 0; 
        for (let i = 1; i < prices.length; i++){
            if (prices[i] > prices[i-1]){
                maxProfit += prices[i] - prices[i-1]
            }
        }
        return maxProfit
    }
}


//TC: O(n) greedy algorithm since we can do unlimited transaction each day. 
