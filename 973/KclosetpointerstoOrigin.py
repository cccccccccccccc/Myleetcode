from typing import List
class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        def gethypotenuse(point):
            return point[0]**2+point[1]**2
        
        points.sort(key=gethypotenuse)
        return points[:K]
A = Solution()
points = [[3,3],[5,-1],[-2,4]]
K = 2
print(A.kClosest(points,K))