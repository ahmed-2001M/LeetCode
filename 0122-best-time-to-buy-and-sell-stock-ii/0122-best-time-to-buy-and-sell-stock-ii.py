class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        s =0 
        
        for i in range(len(prices)-1):
            diff = prices[i+1] - prices[i]

            
            s+=diff if diff > 0 else 0
        return s