class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        lowest_price = float('inf')
        for j in range(1, len(prices)):
            lowest_price = min(lowest_price, prices[j - 1])
            if prices[j] - lowest_price > max_profit:
                max_profit = prices[j] - lowest_price
        return max_profit