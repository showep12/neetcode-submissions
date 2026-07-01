class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #calculate the profit each time 
        
        RP = 0
        #find biggest sale price
        #find smallest buy price
        #compare
        a = [1,2,3]
        
        maxProfit = 0
        for LP in range(len(prices)) : 
              
            if (LP == len(prices) - 1) : 
                return maxProfit
            maxSellPrice = max(prices[LP+1:])
            Profit = maxSellPrice - prices[LP]
            maxProfit = max(Profit, maxProfit)
            #compare each start point 
            # while (profit) : 
            #     profit = 
        return maxProfit