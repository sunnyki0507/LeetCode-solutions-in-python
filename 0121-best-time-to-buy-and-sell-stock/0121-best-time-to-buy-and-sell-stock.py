class Solution(object):
    def maxProfit(self, prices):
        maxN = 0
        buy = max(prices)
        for i in range(len(prices) - 1):
            if buy <= prices[i]:
                continue
            buy = prices[i]
            sell = max(prices[i+1:])
            if (sell - buy) > maxN:
                maxN = sell - buy
            # prev = buy
        return maxN


        """
        :type prices: List[int]
        :rtype: int
        """
        