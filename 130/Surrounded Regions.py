from typing import List
from collections import defaultdict
class Solution:
    def __init__(self):
        self.flag = defaultdict(list)
    def checkregions(self,x,y,board):
        if board[x][y] != "O" or self.flag[(x,y)] == 1 :
            return
        self.flag[(x,y)] = 1
        move = [(1,0),(0,1),(-1,0), (0,-1)]
        for k in range(4):
            nx = x+move[k][0]
            ny = y+move[k][1]
            if nx >= 0 and ny>=0 and nx < len(board) and ny< len(board[0]) and board[nx][ny] =="O": 
                self.checkregions(nx,ny,board)
        return
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if len(board) ==0:
            return
        for i in range(len(board)):
            self.checkregions(i,0,board)
            self.checkregions(i,len(board[0])-1,board)
        for j in range(len(board[0])):
            self.checkregions(0,j,board)
            self.checkregions(len(board)-1,j,board)
        for m in range(len(board)):
            for n in range(len(board[0])):
                if board[m][n] == "O" and (m,n) not in self.flag:
                    board[m][n] = "X"
        return 
A = Solution()
b = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
c = [["O","O"],["O","O"]]
print(A.solve(c))