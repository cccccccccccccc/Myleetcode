"""
timecomplexity = O(m*n) spacecomplexity = O(m*n)
define list of move to spiral in four directions ans is the answer list  
while len(ans) < total number in matrix 
get iterate range by horizon, horizon init is 0 horizon = phase%2 phase has 0,1,2,3 ,4phases .
iterate m or n get x,y index  append item to ans
modify m,n by horizon and modify phase 
 
"""
from typing import List
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        move = [[0,1],[1,0],[0,-1],[-1,0]]
        m = len(matrix)
        n = len(matrix[0])
        ans = []
        phase = 0
        total = m*n
        x = 0
        y = -1
        while len(ans) < total:
            ishorizon = phase%2
            for _ in range(m if ishorizon else n):
                x += move[phase][0]
                y += move[phase][1]
                ans.append(matrix[x][y])
            if ishorizon:
                n-=1
            else:
                m-=1
            phase = (phase+1)%4
        return ans
  
A = Solution()
m = [[1,2,3],[4,5,6],[7,8,9]]
print(A.spiralOrder(m))