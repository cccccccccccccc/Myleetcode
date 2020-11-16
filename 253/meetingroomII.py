from typing import List
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        start = []
        end = []
        for i in intervals:
            start.append(i[0])
            end.append(i[1])
        start.sort()
        end.sort()
        num = 0
        s = e = 0
        while s < len(start):
            if start[s]>=end[e]:
                e+=1
            else:
                num+=1
            s+=1
        return num
A = Solution()
intervals = [[13,15],[1,13]]
print(A.minMeetingRooms(intervals))