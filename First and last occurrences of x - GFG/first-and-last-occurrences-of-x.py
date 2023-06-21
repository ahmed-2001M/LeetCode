#User function Template for python3
import bisect

def find(arr,n,x):
    # code here

    first = bisect.bisect_left(arr, x)
    last = bisect.bisect_right(arr, x) - 1
    if first <= last:
        return [first, last]
    else:
        return [-1, -1]

#{ 
 # Driver Code Starts
t=int(input())
for _ in range(0,t):
    l=list(map(int,input().split()))
    n=l[0]
    x=l[1]
    arr=list(map(int,input().split()))
    ans=find(arr,n,x)
    print(*ans)
# } Driver Code Ends