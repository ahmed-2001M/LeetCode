class Solution:
    def reverseBits(self, n: int) -> int:
        res =0
        for i in range(32):
            res = res<<1|((n>>i)&1)
            
        return res