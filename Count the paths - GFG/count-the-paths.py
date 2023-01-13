#User function Template for python3
from collections import defaultdict
class Solution:
    def possible_paths(self, edges, n, s, d):
        #Code here
        graph =defaultdict(list)
        for parent , child in edges:
            graph[parent].append(child)
        
        def dfs(curr , d):
            if curr == d:
                return 1
            res=0
            for child in graph[curr]:
                res+=dfs(child , d)
            
            return res
        return dfs(s,d)
                

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n, m, s, d = input().split()
		n = int(n); m = int(m); s = int(s); d = int(d);
		edges = []
		for _ in range(m):
		    x,y = input().split()
		    x = int(x); y = int(y);
		    edges.append([x,y])
		obj = Solution()
		ans = obj.possible_paths(edges, n, s, d)
		print(ans)


# } Driver Code Ends