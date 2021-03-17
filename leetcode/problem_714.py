# 714. Best Time to Buy and Sell Stock with Transaction Fee
# Difficulty: Medium
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/

class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        num_days = len(prices)
        buy_prices = [0]*num_days
        buy_prices[0] = -prices[0] - fee
        sell_prices = [0]*num_days
        
        for buy_idx in range(1, num_days):
            buy_prices[buy_idx] = max(buy_prices[buy_idx-1], sell_prices[buy_idx-1] - prices[buy_idx] - fee )
            sell_prices[buy_idx] = max(sell_prices[buy_idx-1], buy_prices[buy_idx-1] + prices[buy_idx])
                                    
        return sell_prices[-1]