from typing import List
class Solution:
    def lowerbound(self,row,m):
        count = 0
        for i in row:
            if i <= m:
                count+=1
            else:
                break
        return count

    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        l = matrix[0][0]
        r = matrix[-1][-1]
        while l < r:
            m = l + (r-l)//2
            total = 0
            for row in matrix:
                total += self.lowerbound(row,m)
            if total>=k:
                r = m
            else:
                l = m+1
        return l