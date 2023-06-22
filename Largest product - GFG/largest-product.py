# You are required to complete this fucntion
# Function should return the an integer
def findMaxProduct(arr, n, m):
    # Code here
    l = 0 
    r = m
    pr = 1
    for i in arr[l:r]:
        pr *=i
    mx = pr
    while r < n:
        pr = pr//arr[l]*arr[r]
        l+=1
        r+=1
        mx = max(mx , pr)
    return mx

#{ 
 # Driver Code Starts
# Your code goes here
if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n,m = map(int, input().strip().split(' '))
        arr = list(map(int, input().strip().split()))
        print (findMaxProduct(arr, n, m))
# } Driver Code Ends