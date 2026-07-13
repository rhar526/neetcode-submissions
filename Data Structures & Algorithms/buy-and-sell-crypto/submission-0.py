class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = prices[0]
        maxProfit = 0
        i = 0
        while i < len(prices):
            l = prices[i] if prices[i] < l else l
            profit = prices[i] - l
            maxProfit = profit if profit > maxProfit else maxProfit
            i += 1

        return maxProfit