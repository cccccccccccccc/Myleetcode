from typing import List
class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        events.sort(key=lambda x:(x[1],x[0]))
        nums = 0
        dayarray=[0]*(10**5+1)
        for i in events:
            for j in range(1,10**5+1):
                if j >i[1]:
                    break
                if j >= i[0] and j <= i[1] and dayarray[j] == 0:
                    dayarray[j] = 1
                    nums+=1 
                    break
        return nums

A = Solution()
a = [[1,2],[2,3],[3,4]]
c = [[1,2],[1,2],[3,3],[1,5],[1,5]]
b =[[1,4],[4,4],[2,2],[3,4],[1,1]]
print(A.maxEvents(c))