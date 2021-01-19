from typing import List
class Solution:
    def isBipartite(self,graph: List[List[int]]) -> bool:
        subsetlist = [0]*len(graph)
        for i in range(len(graph)):
            flag = [0]*3
            for j in graph[i]:
                flag[subsetlist[j]] = 1
            for f in range(1,3):
                if flag[f] == 0:
                    subsetlist[i] = f
                    break
            if subsetlist[i] == 0:
                return False
        return True    
'''
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        subsetlist = [0]*len(graph)
        def dfs(x,graph,subsetlist,flag):
            if subsetlist[x] != 0 :
                if subsetlist[x] != flag:
                    return False
                else:
                    return True
            subsetlist[x] = flag
            for i in graph[x]:
                curans = dfs(i,graph,subsetlist,-flag)
                if curans == False:
                    return curans
            return True
        for k in range(len(graph)):
            if subsetlist[k] == 0 and graph[k] != []:
                ans = dfs(k,graph,subsetlist,1)
                if ans == False:
                    return ans
        return True
'''
A = Solution()
graph = [[1,3],[0,2],[1,3],[0,2]]
graph1 = [[1,2,3],[0,2],[0,1,3],[0,2]]
print(A.isBipartite(graph1))