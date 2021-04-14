from typing import List
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if len(matrix) == 0 or len(matrix[0]) == 0 :
            return 0
        m = len(matrix)
        n = len(matrix[0])
        dp = [[0 for _ in range(n+1)]for _ in range(m+1)]            
        maxsqrlen = 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '1':
                    dp[i][j] = min(dp[i-1][j],dp[i-1][j-1],dp[i][j-1])+1
                    maxsqrlen = max(maxsqrlen,dp[i][j])
        return maxsqrlen**2
A = Solution()
matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
print(A.maximalSquare(matrix))
matrix = [["0","1"],["1","0"]]
print(A.maximalSquare(matrix))
matrix = [["0"]]
print(A.maximalSquare(matrix))