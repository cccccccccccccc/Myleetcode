from typing import List
class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        maxnum = 0
        for i in sorted(boxTypes,key = lambda x:x[1],reverse=True):
            if truckSize==0:
                break
            tmp = min(truckSize,i[0])
            truckSize-=tmp
            maxnum+=tmp*i[1]
        return maxnum
A = Solution()
b=[[1,3],[2,2],[3,1]]
t=4
print(A.maximumUnits(b,t))
b = [[5,10],[2,5],[4,7],[3,9]]
t = 10
print(A.maximumUnits(b,t))
