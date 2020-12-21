from typing import List
#from typing import Interval
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        start , end = newInterval[0],newInterval[1]
        left , right = [],[]
        for i in intervals:
            if i[1]<start:
                left.append(i)
            elif i[0]>end:
                right.append(i) 
            else:
                start = min(start,i[0])
                end = max(end,i[1])
        return left+[[start,end]]+right

A = Solution()
a = [[1,3],[6,9]]
b = [2,5]
print(A.insert(a,b))