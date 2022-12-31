class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mps , mpt = {} , {}

        for i , j in zip(s,t):
            if ((i in mps and mps[i] != j) or (j in mpt and mpt[j] != i )):
                return False
            mps[i] = j
            mpt[j] = i
        return True