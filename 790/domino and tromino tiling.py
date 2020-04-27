#timecomplexity = O(n) spacecomplexity = O(n)
#construct dp, dp[i][0] means 2*i board is full by domino and tromino dp[i][1] means 2*1 board has 1 is not filled
class Solution:
    def numTilings(self, N: int) -> int:
        mk = 100000007
        dp = [[0]*2 for _ in range (N+1)]
        dp[0][0] = dp [1][0] = 1
        for i in range(2,N+1):
            dp[i][0] = (dp[i-1][0] +dp[i-2][0] + dp[i-1][1])%mk
            dp [i][1] = (2*(dp[i-2][0])+dp[i-1][1])%mk
        return dp[N][0]
"""
class Solution:
    def numTilings(self, N: int) -> int:
        mk = 100000007
        dp = [[0]*2 for _ in range (N+1)]
        dp[0][0] = dp [1][0] = 1
        for i in range(2,N+1):
            dp[i][0] = (dp[i-1][0] +dp[i-2][0] + 2*dp[i-1][1])%mk
            dp [i][1] = (dp[i-2][0]+dp[i-1][1])%mk
        return dp[N][0]
"""
A = Solution()
print(A.numTilings())