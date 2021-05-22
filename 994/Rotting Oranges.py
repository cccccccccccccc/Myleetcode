from typing import List
from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        rotdeque = deque()
        count_fresh = 0
        count = 0
        move = [[-1,0],[0,1],[0,-1],[1,0]]
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    rotdeque.append((i,j))
                elif grid[i][j] == 1:
                    count_fresh+=1
        if count_fresh == 0:
            return 0
        while len(rotdeque)>0:
            count +=1
            size = len(rotdeque)
            for i in range(size):
                rot = rotdeque.popleft()
                for c in move:
                    x = c[0]+rot[0]
                    y = c[1]+rot[1]
                    if x < 0 or y < 0 or x >= m or y >= n or grid[x][y] == 0 or grid[x][y] == 2:
                        continue
                    if grid[x][y] == 1:
                        grid[x][y] = 2
                        rotdeque.append((x,y))
                        count_fresh-=1
        return count-1 if count_fresh == 0 else -1
A = Solution()
grid = [[2,1,1],[1,1,0],[0,1,1]]
print(A.orangesRotting(grid))