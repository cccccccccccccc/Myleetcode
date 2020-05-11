from typing import List
from collections import deque
class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
            updatedeque = deque()
            move = [[1,1],[1,0],[0,1],[-1,-1],[0,-1],[-1,0],[1,-1],[-1,1]]
            m = len(board)
            n = len(board[0])
            updatedeque.append(click)
            while len(updatedeque)!= 0:
                check = updatedeque.popleft()
                x,y = check[0],check[1]
                if board[x][y] == 'M':
                    board[x][y] = 'X'
                    break
                if board[x][y] == 'E':
                    count = 0
                    tmplist =[]
                    for k in move:
                        tmpx = x+k[0]
                        tmpy = y+k[1]
                        if tmpx>=0 and tmpx < m and tmpy >=0 and tmpy < n:
                            if board[tmpx][tmpy] == 'M':
                                 count +=1
                            if board[tmpx][tmpy] == 'E':
                                tmplist.append([tmpx,tmpy])
                    if count > 0:
                        board[x][y] = str(count)
                    else:
                        board[x][y] = 'B'
                        if len(tmplist) != 0:
                            for i in tmplist:
                                updatedeque.append(i)
            return board
A = Solution()
a = [["E","E","E","E","E"],["E","E","M","E","E"],["E","E","E","E","E"],["E","E","E","E","E"]]
b = [3,0]
print(A.updateBoard(a,b))