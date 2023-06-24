#User function Template for python3

class Solution:
    def lastIndex(self, s):
        # code here
        mx = -1
        for idx, i in enumerate(s):
            if i == '1':
                mx = idx
        return mx
        



#{ 
 # Driver Code Starts
#Initial Template for Python 3


def main():

    T = int(input())

    while(T > 0):
    	s = input()
    	ob = Solution()
    	print(ob.lastIndex(s))
    	
    	T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends