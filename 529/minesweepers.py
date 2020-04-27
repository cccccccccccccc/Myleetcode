from typing import List
from collections import deque
class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
            updatedeque = deque()
            move = [[1,1],[1,0],[0,1],[-1,-1],[0,-1],[-1,0]]
            m = len(board)
            n = len(board[0])
            updatedeque.append(click)
            while len(updatedeque)!= 0:
                check = updatedeque.popleft()
                if
                for k in move:
                    tmp0 = check[0]+k[0]
                    tmp1 = check[1]+k[1]
                    if tmp0>=0 and tmp0 < m and tmp1 >=0 and tmp1 < n:
                        board