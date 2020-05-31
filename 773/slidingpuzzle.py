from typing import List
from collections import deque
class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        foundstr = set()
        originalstr = ""
        move = [1,-1,3,-3]
        finalstr = "123450"
        possiblestatus = deque()
        for m in range(len(board)):
            for n in range(len(board[m])):
                originalstr += str(board[m][n])
        if originalstr == finalstr:
            return 0
        possiblestatus.append((originalstr,0)) 
        foundstr.add(originalstr)
        while len(possiblestatus)!=0:
            oristatue = possiblestatus.popleft()  
            oristr = oristatue[0]
            oristep = oristatue[1]
            oriindex = oristr.index('0')
            for k in move:
                if k+oriindex >=0 and k+oriindex<len(oristr) and not (oriindex == 2 and k == 1) and not (oriindex == 3 and k == -1):
                    tmp1 = oristr[oriindex]
                    tmp2 = oristr[k+oriindex]
                    tmp = ""
                    for i in range(len(oristr)):
                        if i == oriindex:
                            tmp += tmp2
                        elif i == k+oriindex:
                            tmp += tmp1
                        else:
                            tmp += oristr[i]
                    if tmp == finalstr:
                        return oristep+1
                    if tmp not in foundstr:
                        possiblestatus.append((tmp,oristep+1))
                        foundstr.add(tmp)
        return -1
A = Solution()
a = [[1,2,3],[4,0,5]]
b = [[1,2,3],[5,4,0]]
c = [[4,1,2],[5,0,3]]
d = [[3,2,4],[1,5,0]]
print(A.slidingPuzzle(a))
print(A.slidingPuzzle(b))
print(A.slidingPuzzle(c))
print(A.slidingPuzzle(d))