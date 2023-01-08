class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res =''
        mn = min(strs)
        for i in range(len(mn)):
            for j in strs:
                if j[i] != strs[0][i]:
                    return res
                
            res+=j[i]
        return res