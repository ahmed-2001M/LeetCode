# Function should return an integer value
def convertFive(n):
    # Code here
    res = []
    
    while n:
        f = n%10
        if f == 0:
            res.append(5)
        else:
            res.append(f)
        n//=10
    
    res = res[::-1]
    ans=0
    for i in res:
        ans = ans *10 + i
    return ans

#{ 
 # Driver Code Starts
# Your code goes here
if __name__=='__main__':
    t = int(input())
    for i in range(t):
        print (convertFive(int(input().strip())))
# } Driver Code Ends