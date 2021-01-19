from typing import List
class DSU(object):
    def __init__(self):
        self.pare = list(range(1001))
        self.rk = [0]*(1001)
    def find(self,x):
        if self.pare[x] != x:
            self.pare[x] =self.find(self.pare[x])
        return self.pare[x]
    def union(self,x,y):
        xp,yp = self.find(x),self.find(y)
        if xp == yp:
            return False
        elif self.rk[xp]>self.rk[yp]:
            self.pare[yp] =xp
        elif self.rk[xp]<self.rk[yp]:
            self.pare[xp] = yp
        else:
            self.pare[xp] =yp
            self.rk[yp]+=1
        return True
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        dsu = DSU()
        for edge in edges:
            if dsu.union(*edge) == False:
                return edge
A = Solution()
ed = [[1,2],[1,3],[2,3]]
print(A.findRedundantConnection(ed))