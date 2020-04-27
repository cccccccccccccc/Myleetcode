from typing import List
from collections import deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        numdict = {}
        indegree = [0]*numCourses
        d = deque()
        if prerequisites == []:
            return True
        for n in range(numCourses):
            numdict[n] = []
        for edge in prerequisites:
            key = edge[0]
            v = edge[1]
            indegree[v]+=1
            numdict[key].append(v)
        for i,m in enumerate(indegree):
            if m == 0:
                d.append(i)
        while len(d) != 0:
            cur_v = d.popleft()
            if numdict[cur_v] != []:
                for m in numdict[cur_v]:
                    indegree[m] -= 1
                    if indegree[m] == 0:
                        d.append(m)
        if indegree.count(0) == numCourses:
            return True
        else:
            return False      
A = Solution()
print(A.canFinish(2,[[1,0],[0,1]]))  