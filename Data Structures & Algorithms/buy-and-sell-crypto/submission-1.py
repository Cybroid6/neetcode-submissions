class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        max1 = 0
        for j in range(1 , len(prices)):
            for i , n in enumerate(prices):
                if i + j < (len(prices)):
                    if prices[i+j] - prices[i] > max1:
                        max1 = prices[i + j] - prices[i]
                
        return max1