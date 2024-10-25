class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        i = 0
        j = 0
        max_profit = 0

        while j < len(prices):
            curr_Profit = prices[j] - prices[i]
            if prices[i] < prices[j]:
                max_profit = max(curr_Profit, max_profit)
            else:
                i = j

            j += 1

        return max_profit
