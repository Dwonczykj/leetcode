from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices or len(list(set(prices))) == 1:
            return 0
        n = len(prices)
        max_sell_ind = n-1
        profit = [0 for i in prices]
        # sell_inds = [n-1 for i in prices]
        for i in range(n-1,-1,-1):
            # for each ind i, if i buy at i, from [i+1:] what is the max i  can make, go backwards from end tracking max value before end
            profit[i] = prices[max_sell_ind] - prices[i]
            # sell_inds[i] = max_sell_ind
            # check if current price at i is higher than previous max sale price in rest of price timeseries:
            if prices[max_sell_ind] < prices[i]:
                max_sell_ind = i
        return max(profit)
    
    def maxProfit2(self, prices: List[int]) -> int:

        low = 0
        max = 0

        for high in range(len(prices)):
            profit = prices[high] - prices[low]
            if profit > max:
                max = profit
            if prices[high] < prices[low]:
                low = high
        return max
    
            
    

runner = Solution()

prices = [7,1,5,3,6,4]
output = runner.maxProfit(prices)


prices = [7,6,4,3,1]
output = runner.maxProfit(prices)

prices = [1]
output = runner.maxProfit(prices)
prices = [-1,1]
output = runner.maxProfit(prices) # 2
prices = [1,-1]
output = runner.maxProfit(prices) # 0

debug = True