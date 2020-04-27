"""
from typing import List
class Solution:
    def mesture(self,c:List[float],target:float) ->List[float]:
        for i in range(len(c)):
            c[i] = c[i]*100
        dp = [set()]*(len(c)+1)
        dp[0].add(0)
        valuelist = []
        for i in range(len(c)):
            for j in dp[i]:
                dp[i+1].add(j)
                if j+c[i]<=target:
                    dp[i+1].add(j+c[i])        
        asw = max(dp[-1])
        n = -1
        for m in c[-1:0:-1]:
            n-=1
            if (asw-m) in dp[n]:
                valuelist.append(m/100)
                asw-=m
            
        return valuelist
            

        
A = Solution()
a = [19.99,
8.99,
29.99,
14.99,
29.99,
21.99,
14.99,
14.99,
14.99,
14.99,
14.99,
14.99,
12.99,
14.99,
12.99,
29.99,
8.99,
29.99,
21.99,
12.99,
14.99,
13.99,
15.99,
14.99,
15.99,
15.99,
29.99,
14.99,
12.99,
15.99,
14.99,
15.99,
14.99,
29.99,
8.99,
8.99,
8.99,
29.99,
13.99,
21.99,
12.99,
7.99,
14.99,
79.99,
14.99]

print(A.mesture(a,55200))
"""
from typing import List
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount+1]*(amount+1)
        dp[0] = 0
        for c in coins:
            for j in range(1,amount+1):
                if j-c>=0 :
                    dp[j] = min(dp[j],dp[j-c]+1)
        return dp[amount] if dp[amount] != amount+1 else -1
A = Solution()
a = [2]
b = 3
print(A.coinChange(a,b))

