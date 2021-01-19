from typing import List
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        ans = []
        def dfs(x,graph,curpath):
            if x == len(graph)-1:
                ans.append(curpath.copy())
                return
            for i in graph[x]:
                curpath.append(i)
                dfs(i,graph,curpath)
                curpath.pop()
            return
        dfs(0,graph,[0])
        return ans
A= Solution()
g = [[1,2],[3],[3],[]]
print(A.allPathsSourceTarget(g))