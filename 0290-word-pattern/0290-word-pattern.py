class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split(' ')
        if len(s) != len(pattern) :
            return False
        ms = {}
        mp = {}
        for i,j in zip(pattern,s) :
            if ((i in ms and ms[i]!=j)  or (j in mp and mp[j]!=i)):
                return False
            ms[i] = j
            mp[j] = i
        return True
        