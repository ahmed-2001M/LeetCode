#User function Template for python3
import bisect

def find(arr,n,x):
    left = -1
    right = -1
    
    low = 0
    high = n-1
    while low <= high:
        mid = (low+high)//2
        if arr[mid] == x:
            left = mid
            high = mid-1
        elif arr[mid] < x:
            low = mid+1
        else:
            high = mid-1
    
    if left == -1:
        return [left, right]

    low = left
    high = n-1
    while low <= high:
        mid = (low+high)//2
        if arr[mid] == x:
            right = mid
            low = mid+1
        elif arr[mid] > x:
            high = mid-1
        else:
            low = mid+1

    return [left, right]
    
            
        

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