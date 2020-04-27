from typing import List
class Solution:
    def minSwap(self, A: List[int], B: List[int]) -> int:
        dp = [[0]*2 for _ in range(len(A))]
        dp[0][0] = 0
        dp[0][1] = 1
        for i in range(1,len(A)):
            dp[i][0] = dp[i][1] = float('INF')
            if A[i-1]<A[i] and B[i-1]<B[i]:
                dp[i][0] = dp[i-1][0]
                dp[i][1] = dp[i-1][1]+1
            if A[i-1]<B[i] and B[i-1]< A[i]:
                dp[i][0] = min(dp[i][0],dp[i-1][1])
                dp[i][1] = min(dp[i][1],dp[i-1][0]+1)
        return min(dp[-1][0],dp[-1][1])
A = Solution()
a = [1,3,5,4]
b = [1,2,3,7]
print(A.minSwap(a,b))            
