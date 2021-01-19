from typing import List
class DSU(object):
    def __init__(self,n):
        self.pare = list(range(n))
        self.rk = [0]*(n)
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
    def findCircleNum(self, M: List[List[int]]) -> int:
        num = len(M)
        friendsu = DSU(num)
        for i in range(len(M)):
            for j in range(i+1,len(M)):
                if M[i][j] == 1:
                    friendsu.union(i,j)
        circle = [0]*num
        for x in range(len(M)):
            if circle[friendsu.find(x)]==0:
                circle[friendsu.find(x)] = 1
        return sum(circle)

A = Solution()
a = [[1,1,0],
 [1,1,1],
 [0,1,1]]
print(A.findCircleNum(a))
                
            