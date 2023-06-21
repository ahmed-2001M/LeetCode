#User function Template for python3

class Solution:
    def Maximize(self, a, n): 
        # Complete the function
        a = sorted(a)
        res = 0
        for idx, val in enumerate(a):
            res = int((res + (val * idx) % (1e9+7))% (1e9+7))
        return res
      



#{ 
 # Driver Code Starts
#Initial Template for Python 3


for _ in range(0,int(input())):
    n = int(input())
    arr = list(map(int,input().strip().split()))
    ob=Solution()
    print(ob.Maximize(arr, n))
    
# } Driver Code Ends