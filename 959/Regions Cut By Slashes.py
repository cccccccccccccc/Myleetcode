from typing import List
class DSU(object):
    def __init__(self,n):
        self.parelist = list(range(4*(n**2)))
        self.rank = [0]*(4*(n**2))
    def find(self,x):
        if x != self.parelist[x]:
            self.parelist[x] = self.find(self.parelist[x])
        return self.parelist[x]
    def merge(self,x,y):
        rx = self.find(x)
        ry = self.find(y)
        if rx==ry:
            return
        if self.rank[rx]>self.rank[ry]:
            self.parelist[ry] = rx
        elif self.rank[rx]<self.rank[ry]:
            self.parelist[rx] = ry
        else:
             self.parelist[ry] = rx
             self.rank[rx]+=1
        return
class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        n = len(grid)
        dsu = DSU(n)
        for i in range(n):
            for j in range(n):
                index = 4*(i*n+j) 
                if grid[i][j] == " ":
                    dsu.merge(index,index+1)
                    dsu.merge(index,index+2)
                    dsu.merge(index,index+3)
                elif grid[i][j] == "/":
                    dsu.merge(index,index+3)
                    dsu.merge(index+1,index+2)
                elif grid[i][j] == "\\":
                    dsu.merge(index,index+1)
                    dsu.merge(index+3,index+2)
                if j<n-1:
                    dsu.merge(index+1,index+4+3)
                if i<n-1:
                    dsu.merge(index+2,index+4*n)
        ans=0
        for i in range(4*(n**2)):
            if i == dsu.find(dsu.parelist[i]):
                ans+=1
        return ans  
A = Solution()
a = [" /","/ "]
print(A.regionsBySlashes(a))                    
