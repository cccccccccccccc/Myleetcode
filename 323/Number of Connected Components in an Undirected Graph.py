"""
timecomplexity = O(e*alpha(1)) e is nums of edge. because find and union operation is almost O(1) 
use disjoint set  data stucture 
in this  we iterate all the edges to union nodes together. which will make disjoint set forest. if there are edges between a cluster of nodes there will have the same 
root
then iterate all the node to count how many root there are return the result 
find  recurative to find node's root by check if the node is root of itself. if not recurative to find its root
unionedge compare two node's rank if not the some choose larger one be smaller one's father if same any one be father is ok
"""
from typing import List
class DSU(object):
    def __init__(self,n):
        self.parelist = list(range(n)) # remember each node's root
        self.rank = [0]*n # rank is large means it is high level in the tree.
    def find(self,x):
        if x != self.parelist[x]: 
            self.parelist[x] = self.find(self.parelist[x])
        return self.parelist[x]
    def unionedge(self,x,y):
        rx = self.find(x)
        ry = self.find(y)
        if rx == ry:
            return 
        if self.rank[rx]>self.rank[ry]:
            self.parelist[ry] = rx
        elif self.rank[rx]<self.rank[ry]:
            self.parelist[rx] = ry
        else:
            self.parelist[rx] = ry
            self.rank[ry] +=1
        return 
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        dsu = DSU(n)
        for x,y in edges:
            dsu.unionedge(x,y)
        ans = 0
        for i in range(n):
            if dsu.find(i) == i:
                ans+=1
        return ans
A = Solution()
n = 4
e=[[0,1],[2,3],[1,2]]
print(A.countComponents(n,e))