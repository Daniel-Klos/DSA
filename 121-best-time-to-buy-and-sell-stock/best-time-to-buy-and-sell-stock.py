class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        buy_price = prices[0]
        profit = 0

        for i in range(1, len(prices)):
            cur_price = prices[i]
            if cur_price < buy_price:
                buy_price = cur_price

            profit = max(profit, cur_price - buy_price)

        return profit