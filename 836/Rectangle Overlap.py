from typing import List
class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        overlapbl = [max(rec1[0],rec2[0]),max(rec1[1],rec2[1])]
        overlaptr = [min(rec1[2],rec2[2]),min(rec1[3],rec2[3])]
        if overlapbl[0]<overlaptr[0] and overlapbl[1]<overlaptr[1]:
            return True
        return False
A = Solution()
rec1 = [0,0,2,2]
rec2 = [1,1,3,3]
print(A.isRectangleOverlap(rec1,rec2))
rec1 = [0,0,1,1]
rec2 = [1,0,2,1]
print(A.isRectangleOverlap(rec1,rec2))
rec1 = [0,0,1,1]
rec2 = [2,2,3,3]
print(A.isRectangleOverlap(rec1,rec2))
rec1 = [0,0,1,1]
rec2 = [0,1,1,2]
print(A.isRectangleOverlap(rec1,rec2))
