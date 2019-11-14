"""
time complexity = O(nlogn),space complexity = O(n)

if list is null return

iterate sorted list by every element's start 

if answer list is empty or the last one's end in answer bigger than current element's start:  append
else max last one's end in auswerlist , current element's start

"""
from typing import List
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals)<=0:
            return intervals
        ans = []
        for i in sorted(intervals,key = lambda x:x[0]):
            if not ans or ans[-1][1] < i[0]:
                ans.append(i)
            else:
                ans[-1][1] = max(ans[-1][1],i[1])
        return ans

A = Solution()
a = [[1,3],[2,6],[8,10],[9,11]]
b = [[1,4],[2,3],[9,11],[8,10]]
print(A.merge(b))
