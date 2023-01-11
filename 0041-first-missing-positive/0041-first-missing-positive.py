class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        mx = max(nums)
        
        
        mp = {}
        
        for i in nums:
            if i > 0:
                mp[i]=1
        for i in range(1,2**31):
            if not mp.get(i):
                return i
        return mx+1
        
        
        # total = mx*(mx+1)//2
        # sm = 0
        # for i in nums:
        #     if i >0:
        #         sm+=i
        # if total - sm ==0:
        #     return mx+1
        # return total - sm