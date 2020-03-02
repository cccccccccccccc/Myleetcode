class Solution:
    def judgeCircle(self, moves: str) -> bool:
        movedict = {'L':0,'R':0,'U':0, 'D':0}
        for i in moves:
            movedict[i]+=1
        return movedict['L'] == movedict['R'] and movedict['U'] == movedict['D']