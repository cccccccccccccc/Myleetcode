from typing import List
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0]*(amount+1)
        dp [0] = 1
        for i in coins:
            for j in range(1,amount+1):
                if j-i>=0:
                    dp[j] +=dp[j-i]
        return dp[-1]
A = Solution()
a = 5
b = [1,2,5]
print(A.change(a,b))
