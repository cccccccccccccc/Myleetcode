from typing import List
class DSU:
    def __init__(self,n):
        self.parents = [i for i in range(n)]
        self.rank = [0]*n
    def find(self,x):
        if x!= self.parents[x]:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]
    def unioncity(self,x,y):
        rx= self.find(x)
        ry = self.find(y)
        if rx != ry:
            if rx>ry:
                self.parents[y]= rx
                self.rank[x]+=1
            else:
                self.parents[x] = ry
                self.rank[y] +=1
        else:
            self.parents[y] = rx
            self.rank[x]+=1
        return
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        dsu = DSU(n)
        for i in range(n):
            for j in range(n):
                if i!=j and isConnected[i][j]==1:
                    dsu.unioncity(i,j)
        ans = 0
        for m in range(n):
            if dsu.parents[m] != m:
                ans+=1
        return ans
            
A = Solution()
isConnected = [[1,1,0],[1,1,0],[0,0,1]]
print(A.findCircleNum(isConnected))
            