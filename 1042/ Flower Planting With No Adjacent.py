from typing import List
from collections import defaultdict
class Solution:
    def gardenNoAdj(self, n: int, paths: List[List[int]]) -> List[int]:
        graph = [[]for i in range(n+1)]
        def colorchange(color):
            color +=1 
            if color==5:
                color = 1
            return color
        for x in paths:
            graph[x[0]].append(x[1])
            graph[x[1]].append(x[0])
        anslist = [0]*(n+1)  
        for i in range(1,n+1):
            color = [0]*5
            for j in graph[i]:
                color[anslist[j]] = 1
            for c in range(1,5):
                if color[c] == 0:
                    anslist[i] = c
                    break
        return anslist[1:]
"""
        gardenque = deque()           
            if anslist[i]== 0:
                anslist[i] = 1
                gardenque.append(i)
                while len(gardenque)!= 0:
                    curgarden = gardenque.popleft()
                    curcolor = anslist[curgarden]
                    nextcolor = colorchange(curcolor)
                    for j in graph[curgarden]:
                        if anslist[j] == 0:
                            anslist[j] = nextcolor
                            nextcolor = colorchange(nextcolor)
                            gardenque.append(j)
        return anslist[1:]
"""               
A = Solution()
n = 5
paths = [[4,1],[4,2],[4,3],[2,5],[1,2],[1,5]]
m =4
p =[[1,2],[3,4],[3,2],[4,2],[1,4]]
print(A.gardenNoAdj(m,p))