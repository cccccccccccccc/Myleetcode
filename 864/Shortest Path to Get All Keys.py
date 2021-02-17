from typing import List
from collections import deque
class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:
        n, m = len(grid),len(grid[0])
        numofkey = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == "@":
                    startx= i
                    starty = j
                if grid[i][j] in "abcdef":
                    numofkey +=1
        visited = set()
        dequrekey = deque()
        dequrekey.append((startx,starty,0,".@abcdef",0))
        dir = [[1,0],[0,1],[-1,0],[0,-1]]
        while len(dequrekey)>0:
            x,y,steps,keys,numkey = dequrekey.popleft()
            if grid[x][y] in "abcdef" and grid[x][y].upper() not in keys:
                keys+= grid[x][y].upper()
                keys = "".join(sorted(keys))
                numkey+=1
            if numkey == numofkey: return steps
            for i,j in dir:
                nx = x+i 
                ny = y+j
                if 0<=nx<n and 0<=ny<m and grid[nx][ny] in keys:
                    if (nx,ny,keys) not in visited:
                        visited.add((nx,ny,keys))
                        dequrekey.append((nx,ny,steps+1,keys,numkey))
        return -1

A = Solution()
print(A.shortestPathAllKeys(["@.a.#","###.#","b.A.B"]))
print(A.shortestPathAllKeys(["@..aA","..B#.","....b"]))