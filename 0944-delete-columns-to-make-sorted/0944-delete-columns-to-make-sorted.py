class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        res =0
        for i in range(len(strs[0])):
            flag = 0
            for j in range(len(strs)-1):
                if strs[j][i] > strs[j+1][i]:
                    flag=1
            if flag :
                res+=1
        return res