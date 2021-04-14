from typing import List
class Solution:
    def getreordernum(self,city,topolist,cityset):
        if city in cityset:
            return
        cityset.add(city)
        for r in topolist[city]:
            if r[0] not in cityset:
                if r[1] == 1:
                    self.reordernum+=1
                self.getreordernum(r[0],topolist,cityset)
        return
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        topolist = [[]for _ in range(n)]
        cityset = set()
        self.reordernum =0
        for route in connections:
            topolist[route[0]].append((route[1],1))
            topolist[route[1]].append((route[0],0))
        self.getreordernum(0,topolist,cityset)
        return self.reordernum
A = Solution()
n = 5
c= [[1,0],[1,2],[3,2],[3,4]]
print(A.minReorder(n,c))