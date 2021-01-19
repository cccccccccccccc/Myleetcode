from typing import List
from collections import defaultdict
from collections import deque
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        inbound = [0]*numCourses
        path = defaultdict(list)
        for m,n in prerequisites:
            inbound[m]+=1
            path[n].append(m)
        course = deque()
        for i in range(numCourses):
            if inbound[i] == 0:
                course.append(i)
        ans = []
        while len(course)!=0:
            curcourse = course.popleft()
            for j in path[curcourse]:
                inbound[j] -=1
                if inbound[j] == 0:
                    course.append(j)
            ans.append(curcourse)
        return ans if len(ans)== numCourses else []
A = Solution()
numCourses = 3
prerequisites = [[1,0],[1,2],[0,1]]
print(A.findOrder(numCourses,prerequisites))