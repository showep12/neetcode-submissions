class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #calculate the profit each time 
        LP, RP = 0,1
        maxProfit = 0

        #find the lower buy price
        #in the buy price, compare selling prices

        #maxProfit = max(profit, maxProfit)
        # “Set maxProfit to the maximum of profit and maxProfit.”
        # Update maxProfit with the larger of profit and the current maxProfit.”
        # We keep track of the maximum profit seen so far.”
        while (RP < len(prices)) :
            if (prices[LP] < prices[RP]) : #if the selling price is greater than buying price
                #calculate the profit and update the maxProfit
                profit = prices[RP] - prices[LP]
                maxProfit = max(profit, maxProfit) 
                #Update the maxProfit with the larget of profit and maxProfit
                #we keep track of the maximum profit seen so far
            else : #During loop, if there is smaller value exist, switch the buying date
                LP = RP
            RP+= 1
            
        return maxProfit


"""
maxProfit = max(profit, maxProfit) 어떻게 읽나?
🔹 가장 표준적이고 자연스러운 표현 (면접용)

“Set maxProfit to the maximum of profit and maxProfit.”

📌 이게 가장 정확하고 안전해.

🔹 조금 더 구어체로

“Update maxProfit with the larger of profit and the current maxProfit.”

📌 sliding window / greedy 설명할 때 특히 좋음.

🔹 의미 중심으로 풀어서

“We keep track of the maximum profit seen so far.”

📌 사실 면접에서 제일 좋은 표현은 이거다.
수식보다 의도를 말함.
"""