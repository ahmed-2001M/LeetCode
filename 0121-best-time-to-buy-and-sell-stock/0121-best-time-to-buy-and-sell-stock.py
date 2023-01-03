class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mn = prices[0]
        prof = 0
        
        for idx , i in enumerate(prices):
            diff = i - mn
            #maximize profit
            prof = max(prof , diff)
            #update minimum value
            if i < mn:
                mn = prices[idx]
        return prof
                
                
        