from typing import List
class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        newintervals = []
        for i in intervals:
            newintervals.append((i[0],1))
            newintervals.append((i[1],-1))
        newintervals.sort()
        count = 0
        for k in newintervals:
            count +=k[1]
            if count >1:
                return False
        return True
A = Solution()
intervals = [[13,15],[1,13]]
print(A.canAttendMeetings(intervals))