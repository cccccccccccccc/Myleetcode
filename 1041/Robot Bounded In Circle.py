from typing import List
class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        directions=[[0,1],[1,0],[0,-1],[-1,0]]
        x= y = 0
        idx = 0
        for i in instructions:
            if i == 'L':
                idx = (idx+3)%4
            elif i == 'R':
                idx = (idx +1)%4
            else:
                x +=directions[idx][0]
                y +=directions[idx][1]
        return (x ==0 and y == 0)or idx != 0
A = Solution()
print(A.isRobotBounded("GL"))