from typing import List
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        maxtime = 100*101
        distance = [maxtime]*n
        distance[k-1] = 0
        for i in range(n):
            for u,v,w in times:
                distance[v-1] = min(distance[v-1],distance[u-1]+ w)
        ans=max(distance)
        return ans if ans < maxtime else -1
A=Solution()
times = [[1,2,1]]
n = 2
k = 2
print(A.networkDelayTime(times,n,k))