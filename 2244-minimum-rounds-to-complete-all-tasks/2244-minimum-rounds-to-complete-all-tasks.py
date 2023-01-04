class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        
        mp = {}
        res = 0
        for i in tasks:
            mp[i] = mp[i]+1 if mp.get(i) else 1
        for k , val in mp.items():
            if val == 1:
                return -1
            if val % 3 == 0:
                res +=val//3
            else:
                res += val//3 +1
        return res
                
            