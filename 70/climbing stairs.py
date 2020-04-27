#timecomplexity = O(n) spacecomplexity = O(1)
"""
class Solution:
    def climbStairs(self, n: int) -> int:
        dp1=dp2 = 1
        for tmp in range(2,n+1):
            dp2,dp1 = dp1+dp2,dp2
        return dp2
"""
#timpcomplexity = O(n) spacecomplxity = O(n)
"""
use memory dict to keep the f(m) which has been used before.  
"""
class Solution:
    def _climbStairs(self, n:int)->int:
        if n<=1 :
            return 1
        if n not in self.mem:
            self.mem[n] = self.climbStairs(n-1)+ self.climbStairs(n-2)
        return self.mem[n]
    def climbStairs(self, n:int)->int:
        self.mem = {}
        return self._climbStairs(n)


A = Solution()
q =3
print(A.climbStairs(2))