"""
timecomplexity = O(nlog(n)) n is points.length 
sort the list by function to get k closet points in list
"""
from typing import List
class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        def getdistance(point):
            return point[0]**2+point[1]**2
        points.sort(key=getdistance)
        return points[:K]
A = Solution()
points = [[3,3],[5,-1],[-2,4]]
K = 2
print(A.kClosest(points,K))