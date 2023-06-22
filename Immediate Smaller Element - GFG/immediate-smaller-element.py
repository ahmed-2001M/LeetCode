#User function Template for python3
class Solution:

	def immediateSmaller(self,arr,n):
		# code here
		for idx , val in enumerate(arr[1:]):
		    if val < arr[idx]:
		        arr[idx] = val
		    else:
		        arr[idx] = -1
		arr[-1] = -1
		return arr


#{ 
 # Driver Code Starts
if __name__ == '__main__':
    tcs=int(input())

    for _ in range(tcs):
        n=int(input())
        arr=[int(x) for x in input().split()]
        ob = Solution()
        ob.immediateSmaller(arr,n)
        for x in arr:
            print(x, end=" ")
        print()
# } Driver Code Ends