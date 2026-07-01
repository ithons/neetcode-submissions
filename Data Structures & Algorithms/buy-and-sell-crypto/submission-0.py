def recursiveMaxProfit(prices):
    if len(prices) < 2: return max(prices), 0
    maximum, profit = recursiveMaxProfit(prices[1:])
    price_now = prices[0]
    buy = maximum-price_now
    if buy>profit: profit = buy
    if price_now>maximum: maximum = price_now
    return maximum, profit

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maximum, profit = recursiveMaxProfit(prices)
        return profit