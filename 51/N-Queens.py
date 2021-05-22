"""
timecomplexity = O()  spacecomplexity = O(n)
dfs 
remained col hill datel diagonals in dict iterate each row try to add a queen check col hill datel diagonals if it is ok continue after recusive remove queen and col diagonals dict value
"""
from typing import List
class Solution:
    def dfsNQueens(self,n,r,col,hill,dale,answer):
        if r == n:
            tmp = []
            for i in range(n):
                curstr = ""
                for j in range(n):
                    curstr+=answer[i][j]
                tmp.append(curstr)
            self.answers.append(tmp)
            return
        for i in range(n):
            if i not in col and r+i not in hill and r-i not in dale:
                answer[r][i] = "Q"
                col.add(i)
                hill.add(r+i)
                dale.add(r-i)
                self.dfsNQueens(n,r+1,col,hill,dale,answer)
                answer[r][i] ="."
                col.remove(i)
                hill.remove(r+i)
                dale.remove(r-i)
        return
    def solveNQueens(self, n: int) -> List[List[str]]:
        if n == 1 :
            return [["Q"]]
        self.answers = []
        answer = [['.'for _ in range(n)]for _ in range(n)]
        col = set()
        hill = set()
        dale = set()
        self. dfsNQueens(n,0,col,hill,dale,answer)
        return self.answers
A = Solution()
n = 4
print(A.solveNQueens(n))