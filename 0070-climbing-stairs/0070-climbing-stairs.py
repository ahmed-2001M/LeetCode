class Solution:
    def climbStairs(self, n: int) -> int:
        dp={}
        def solve(m):
            if dp.get(m):
                return dp[m]
            if m == 1 or m==2:
                return m
            dp[m] = solve(m-1) + solve(m-2)
            return dp[m]
        return solve(n)

            
        