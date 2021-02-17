from typing import List
import heapq
class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        event = sorted((l,-h,r) for l,r,h in buildings + list({(r,0,0) for _,r,_ in buildings}))
        ret = [[0,0]]
        hp = [(0,float('inf'))]
        heapq.heapify(hp)
        for l, negh ,r in event:
            if negh:
                heapq.heappush(hp,(negh,r))
            while hp[0][1]<= l:
                heapq.heappop(hp)

            if ret[-1][1] != -hp[0][0]:
                ret.append([l,-hp[0][0]])
        return ret[1:]

A = Solution()
b = [[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]
c = [[1,5,3],[2,3,5],[4,6,2]]
print(A.getSkyline(c))