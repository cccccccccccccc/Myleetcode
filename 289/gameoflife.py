from typing import List
class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if len(board) <= 0:
            return
        m = len(board)
        n = len(board[0])
        newboard = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                sum = 0
                if i-1 >= 0:
                    sum += board[i-1][j]
                    if j-1 >= 0:
                        sum += board[i-1][j-1]
                    if j+1 < n:
                        sum += board[i-1][j+1]
                if j-1 >= 0:
                    sum += board[i][j-1]
                if j+1 < n:
                    sum += board[i][j+1]
                if i+1 < m:
                    sum += board[i+1][j]
                    if j-1 >= 0:
                        sum += board[i+1][j-1]
                    if j+1 < n:
                        sum += board[i+1][j+1]
                if board[i][j] == 1 and (sum < 2 or sum > 3):
                    newboard[i][j] = 0
                elif board[i][j] == 0 and sum ==3:
                    newboard[i][j] = 1
                else:
                    newboard[i][j] = board[i][j]
        for i in range(m):
            for j in range(n):
                board[i][j] = newboard[i][j]
        
        return 
A = Solution()
a = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
print(A.gameOfLife(a))
print(a)
