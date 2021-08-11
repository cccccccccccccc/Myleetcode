"""
timecomplexity =O(n) spacecomplexity = O(1)
if the Robot can have a circle in its rail, it needs to go back to [0,0] or its face shoud not turn to north after a series of moves 
use a list to store direction for robot
use idx 0 to 3 to separate four side 0 is north 1 is right 3 is left 
iterate instrctions to change idx by direction.
at least check if it reach the target back to [0,0] or not face to north 
"""
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


class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        direction = [[0,1],[1,0],[0,-1],[1,0]]
        idx = 0
        x = 0
        y = 0
        for i in instructions:
            if i == "L":
                idx = (idx+1)%4
            elif i == "R":
                idx = (idx+3)%4
            else:
                x += direction[idx][0]
                y += direction[idx][1]
        return (x == 0 and y == 0) or idx!= 0
A = Solution()
print(A.isRobotBounded("GL"))