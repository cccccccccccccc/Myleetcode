"""
timecompliexty = O(nlog(n))
separate start and end time into two list 
sort each of them
use s,e represent start and end index from 0
iterate start time list by while loop 
compare start[s] end[e]
if start >= end means after cur meeting finish another one can use the meeting room ,no need to add a new room
else means before current meeting finish another one need to use room so need add a new one
move two index s,e by compare and add num of meeting when a new room is needed
"""
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