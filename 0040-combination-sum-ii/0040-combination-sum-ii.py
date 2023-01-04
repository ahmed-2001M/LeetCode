
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        def dfs(i , ls , total):
            if total == target and ls not in res:
                res.append(ls.copy())
            if i >= len(candidates) or total > target:
                return
            prev = -1
            for i in range(i,len(candidates)):
                if candidates[i] == prev:
                    continue
                ls.append(candidates[i])
                dfs(i+1 , ls , total + candidates[i])
                ls.pop()
                prev = candidates[i]
            
            dfs(i+1 , ls , total)
        dfs(0,[],0)


        return res
    
