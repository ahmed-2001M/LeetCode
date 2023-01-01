class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res =0
        sset = set()
        idx = 0
        for val  in s:
            while val in sset:
                sset.remove(s[idx])
                idx +=1
            sset.add(val)
            res = max(res, len(sset))
        res = max(res , len(sset))
        return res

        
        