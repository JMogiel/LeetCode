class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        i = 0
        total_profit = []
        total_loss = []

        for j in range(1, len(prices)):
            profit = prices[j] - prices[i]
            if profit >= 0:
                total_profit.append(profit)
            else:
                total_loss.append(profit)

            i += 1

        x = sum(total_profit)
        return x
