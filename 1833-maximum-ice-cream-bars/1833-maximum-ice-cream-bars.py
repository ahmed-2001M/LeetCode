class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs = sorted(costs)
        res =0
        for i in costs:
            if coins >=i:
                res+=1
                coins = coins - i
            else:
                return res
        return res