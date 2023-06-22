# Your task is to complete this function
# Function should return an integer
def num(arr, n, k):
    res = 0
    # Code here
    for i in arr:
        b = i
        while b:
            f = b%10
            if f == k:
                res +=1
            b//=10
    return res


#{ 
 # Driver Code Starts
if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        k = int(input())
        print(num(arr, n, k))
# Contributed By: Harshit Sidhwa

# } Driver Code Ends