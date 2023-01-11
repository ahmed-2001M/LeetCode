#User function Template for python3

class Solution:
    
    #Function to return a list containing the DFS traversal of the graph.
    def dfsOfGraph(self, V, adj):
        # code here
        vis = []
        mp = {}
        res =[]
        for idx,ad in enumerate(adj):
            mp[idx]=ad

        def dfs(cur , par):
            res.append(cur)
            vis.append(cur)
            for child in mp[cur]:
                if child not in vis:
                    dfs(child,cur)
            return res
        return dfs(0,-1)
                

#{ 
 # Driver Code Starts
if __name__ == '__main__':
    T=int(input())
    while T>0:
        V,E=map(int,input().split())
        adj=[[] for i in range(V+1)]
        for i in range(E):
            u,v=map(int,input().split())
            adj[u].append(v)
            adj[v].append(u)
        ob=Solution()
        ans=ob.dfsOfGraph(V,adj)
        for i in range(len(ans)):
            print(ans[i],end=" ")
        print()
        T-=1
# } Driver Code Ends