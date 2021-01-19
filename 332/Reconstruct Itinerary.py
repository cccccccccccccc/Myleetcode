from typing import List
from collections import defaultdict
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        ticket = defaultdict(list)
        for fr, to in tickets:
            ticket[fr].append(to)
        for k in ticket.keys():
            ticket[k].sort(reverse = True)
        ans = []
        def dfs(f,ans):
            while len(ticket[f]) != 0:
                pre = ticket[f].pop()
                dfs(pre,ans)
            ans.append(f)
        dfs("JFK",ans)
        ans.reverse()
        return ans

A = Solution()
f = [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]
c = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
print(A.findItinerary(c))
