class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit=float("-inf")
        buy=0

        for i in range(len(prices)):


            max_profit=max(prices[i]-prices[buy],max_profit)

            if prices[i]<prices[buy]:
                buy=i
        return max_profit