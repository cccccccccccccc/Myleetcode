from typing import List
from collections import deque
class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        foundstr = set()
        originalstr = ""
        possiblestatus = deque()
        for m in range(len(board)):
            for n in range(len(board[m])):
                originalstr += str(board[m][n])