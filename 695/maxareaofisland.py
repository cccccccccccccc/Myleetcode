from typing import List
class Solution:
    def getarea(self, x, y, grid):
        count = 0
        if grid[x][y] == 0:
            return count
        move = [[1,0],[-1,0],[0,1],[0,-1]]
        count += 1
        grid[x][y] = 0
        for k in move:
            tmpx = k[0]+x
            tmpy = k[1]+y
            if tmpx>=0 and tmpx<len(grid) and tmpy >=0 and tmpy<len(grid[0]):
                count+=self.getarea(tmpx,tmpy,grid)
        return count

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0]) 
        maxarea = 0
        for i in range(m):
            for j in range(n):
                maxarea = max(maxarea,self.getarea(i,j,grid))
        return maxarea
A  = Solution()
a = [[1,1,0,0,0],[1,1,0,0,0],[0,0,0,1,1],[0,0,0,1,1]]
b = [[0,0,1,0,0,0,0,1,0,0,0,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,1,1,0,1,0,0,0,0,0,0,0,0],
 [0,1,0,0,1,1,0,0,1,0,1,0,0],
 [0,1,0,0,1,1,0,0,1,1,1,0,0],
 [0,0,0,0,0,0,0,0,0,0,1,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,0,0,0,0,0,0,1,1,0,0,0,0]]
c = [[0,1],[1,1]]
print(A.maxAreaOfIsland(a))
print(A.maxAreaOfIsland(b))
print(A.maxAreaOfIsland(c))