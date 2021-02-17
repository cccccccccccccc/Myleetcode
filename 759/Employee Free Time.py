from typing import List
import heapq
# Definition for an Interval.
class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end


class Solution:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        allinterval = []
        heapq.heapify(allinterval)
        ans = []
        for i,e in enumerate(schedule):
            heapq.heappush(allinterval,(e[0].start,e[0].end,i,0))
        interval = Interval()
        flag = False
        freetime = []
        while len(allinterval)>0:
            cur = heapq.heappop(allinterval)
            id = cur[2]
            idx = cur[3]
            if flag == False:
                interval = Interval(cur[0],cur[1])
                flag = True
            else:
                if cur[0]>interval.end:
                    freetime.append(Interval(interval.end,cur[0]))
                    interval.start = cur[0]
                    interval.end = cur[1]
                else:
                    interval.end = max(interval.end,cur[1])
            if len(schedule[id])-1>idx:
                heapq.heappush(allinterval,(schedule[id][idx+1].start,schedule[id][idx+1].end,id,idx+1))
        return freetime

i1 = Interval(1,2)
i2 = Interval(6,7)
i3 = Interval(2,4)
i4 = Interval(2,5)
i5 = Interval(9,12)
A = Solution()
print(A.employeeFreeTime([[i1,i2],[i3],[i4,i5]]))