from typing import List
import heapq
class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        cur = startFuel
        stops = 0
        i = 0
        fuelstops = []
        heapq.heapify(fuelstops)
        while True:
            if cur>= target: return stops
            while i < len(stations) and stations[i][0]<= cur:
                heapq.heappush(fuelstops,-stations[i][1])
                i+=1
            if len(fuelstops) == 0:
                break
            cur+= -heapq.heappop(fuelstops)
            stops+=1
        return -1
A = Solution()
print(A.minRefuelStops(1,1,[]))