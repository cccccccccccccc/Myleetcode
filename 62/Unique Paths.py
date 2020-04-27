#timecomplexity = O(MN) spacecomplexity = O(MN)
"""
paddings required to handle out of board cases
Actural indes start from 1 instead of 0
remeber dp[1][1] is 1 and no need to define by loop
for dp array the first [] is row the second [] is column
"""
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0]*(m+1)for _ in range(n+1)]
        dp[1][1] = 1
        for i in range(1,n+1):
            for j in range(1,m+1):
                if i ==1 and j == 1:
                    continue
                else:
                    dp[i][j] = dp[i][j-1]+ dp[i-1][j]
        return dp[n][m]
A = Solution()
print(A.uniquePaths(3,2))