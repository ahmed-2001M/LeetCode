class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        res = []
        def dfs(i , ls , total):
            
            if total == target:
                res.append(ls.copy())
                return
            if i>=len(candidates) or total > target:
                return
            
            ls.append(candidates[i])
            dfs(i , ls , total + candidates[i])
            ls.pop()
            dfs(i+1 , ls , total)
        dfs(0,[],0)
        return res
            
        