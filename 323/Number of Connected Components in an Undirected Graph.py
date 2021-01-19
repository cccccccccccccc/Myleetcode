from typing import List
class DSU(object):
    def __init__(self,n):
        self.parelist = list(range(n))
        self.rank = [0]*n
    def find(self,x):
        if x != self.parelist[x]:
            self.parelist[x] = self.find(self.parelist[x])
        return self.parelist[x]
    def unionedge(self,x,y):
        rx = self.find(x)
        ry = self.find(y)
        if rx == ry:
            return 
        if self.rank[rx]>self.rank[ry]:
            self.parelist[ry] = rx
        elif self.rank[rx]<self.rank[ry]:
            self.parelist[rx] = ry
        else:
            self.parelist[rx] = ry
            self.rank[ry] +=1
        return 
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        dsu = DSU(n)
        for x,y in edges:
            dsu.unionedge(x,y)
        ans = 0
        for i in range(n):
            if dsu.find(i) == i:
                ans+=1
        return ans
A = Solution()
n = 4
e=[[0,1],[2,3],[1,2]]
print(A.countComponents(n,e))