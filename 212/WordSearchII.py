from typing import List
from collections import defaultdict
class Trie:
    def __init__(self):
        self.node = defaultdict(Trie)
        self.word = None

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = Trie()
        for w in words:
            p = root
            for c in w:
                if c not in p.node.keys():
                    p.node[c] = Trie()
                p = p.node[c]
            p.word = w
        m,n = len(board),len(board[0])
        self.flag = set()
        answer = []
        self.numword = len(words)
        for i in range(m):
            for j in range(n):
                if board[i][j] in root.node.keys():
                    self.flag.add((i,j))
                    self.dfsword(i,j,board,root.node[board[i][j]],answer)
                    self.flag.remove((i,j))
        return answer
    def dfsword(self,i,j,board,childnode,answer):
        if self.numword == 0:
            return
        if childnode.word != None:
            answer.append(childnode.word)
            childnode.word = None
            self.numword -=1
        move = [[1,0],[0,1],[-1,0],[0,-1]]
        for k in move:
            x = i+k[0]
            y = j+k[1]
            if x>=0 and y>= 0 and x < len(board) and y<len(board[0]) and (x,y) not in self.flag and board[x][y] in childnode.node.keys():
                self.flag.add((x,y))
                self.dfsword(x,y,board,childnode.node[board[x][y]],answer)
                self.flag.remove((x,y))
A = Solution()
board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]]
words = ["oath","pea","eat","rain"]
print(A.findWords(board,words))