from typing import List
class Solution:
    def getcost(self,l,r,cost):
        sum = 0
        maxcost = 0
        for m in range(l,r+1):
            maxcost = max(maxcost,cost[m])
            sum+=cost[m]
        return sum-maxcost
    def minCost(self, s: str, cost: List[int]) -> int:
        l = 0 
        r = 1
        ln = len(s)
        minsum = 0
        while r<ln:
            if s[l] != s[r]:
                if l+1<r:
                    minsum+=self.getcost(l,r-1,cost)
                    l = r
                    r = r+1
                else:
                    l+=1
                    r+=1
            elif s[l] == s[r]:
                if r == ln-1:
                    minsum+= self.getcost(l,r,cost)
                r+=1
        return minsum
A = Solution()
s = "abaac"
c = [1,2,3,4,5]
print(A.minCost(s,c))