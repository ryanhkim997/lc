from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # output:
            # int representing max profit, else 0
        # input:
            # array of prices, where i is the ith day, prices[i] is the price
        # constraints:
            # 1 <= prices.length <= 105
            # 0 <= prices[i] <= 104
        # edge cases:
            # array is never empty
            # buying and selling on same day (prices len 1) gives you zero
        

        # want to find greatest difference (prices[j] - prices[i])

        i = 0
        j = 1
        profit = 0

        while j < len(prices):
            # bulk of logic
            temp_profit = prices[j] - prices[i]

            if prices[j] > prices[i]:
                profit = max(temp_profit, profit)
            else: i = j

            j += 1


        return profit