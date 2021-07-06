from typing import List
class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        if len(jobDifficulty) < d:
            return -1
        job= len(jobDifficulty)  
        dp = [[10001 for _ in range(job+1)] for _ in range(d+1)] 
        dp[0][0] = 0
        for i in range(1,d+1):
            for j in range(1,job+1):
                #for x in range(i-1,j):
                maxd = 0
                for x in range(j-1,-1,-1):
                    maxd = max(maxd,jobDifficulty[x])
                    dp[i][j] = min(dp[i][j],(dp[i-1][x]+maxd))

        return dp[d][job]
A = Solution()
j = [11,111,22,222,33,333,44,444]
#[6,5,4,3,2,1]


d = 6
#d=2
print(A.minDifficulty(j,d))