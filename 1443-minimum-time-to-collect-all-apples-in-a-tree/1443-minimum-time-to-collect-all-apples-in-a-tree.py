class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        mp = {i:[] for i in range(n)}
        
        for par , child in edges:
            mp[par].append(child)
            mp[child].append(par)
        
        def dfs(cur , par):
            time =0
            
            for i in mp[cur]:
                if i == par:
                    continue
                t1 = dfs(i,cur)
                if t1 or hasApple[i]:
                    time+=2+t1
            return time
        return dfs(0,-1)
        