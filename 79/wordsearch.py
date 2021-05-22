"""
timecomplexity = O(N*3^L)N is all the cells in grid L is length of word iterate all the cell in grid and each grid we have 3 direction(we cannot go back to where we come from)
spacecomplexity = O(L) which flag use to contain grid is used
use dfs
flag set to check if is used grid
iterate m, n in grid  mark flag  go dfs to check if there is a way  after remove the flag
in dfs  if cur grid'value is not equal to word index( which is take by dfs to remember the index)
move four direction check if is in range and if the new grid is used if not continue dfs 
remember each time remove flag after operate.
return answer
"""
from typing import List
class Solution:
    def dfsword(self, i,j,board,index,word):
        if board[i][j] != word[index]:
            return False
        if index == len(word)-1:
            return True
        move = [[1,0],[0,1],[-1,0],[0,-1]]
        cur = False
        for k in move:
            x = i+k[0]
            y = j+k[1]
            if x>=0 and y>= 0 and x < len(board) and y<len(board[0]) and (x,y) not in self.flag :
                self.flag.add((x,y))
                cur = self.dfsword(x,y,board,index+1,word)
                if cur == True:
                    return cur
                self.flag.remove((x,y))
        return cur
    def exist(self, board: List[List[str]], word: str) -> bool:
        m,n = len(board),len(board[0])
        self.flag = set()
        isexist = False
        for i in range(m):
            for j in range(n):
                self.flag.add((i,j))
                isexist = self.dfsword(i,j,board,0,word)
                if isexist == True:
                    return isexist
                self.flag.remove((i,j))
        return isexist
A = Solution()
board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "ABCCED"
print(A.exist(board,word))