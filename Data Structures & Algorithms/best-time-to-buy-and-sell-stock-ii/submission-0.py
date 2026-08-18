class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for n in range(1, len(prices)):
            if prices[n] > prices[n-1]:
                profit+=prices[n]-prices[n-1]
        return profit
