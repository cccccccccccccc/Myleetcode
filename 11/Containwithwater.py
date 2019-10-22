from typing import List
class Solution:
    def maxArea(self, height: List[int]) -> int:
        Lbegin = 0
        Lend = len(height)-1
        maxarea = 0
        while Lbegin != Lend:
            tmpH = min(height[Lbegin],height[Lend])
            tmparea = tmpH * (Lend-Lbegin)
            if maxarea < tmparea:
                maxarea = tmparea
            if tmpH == height[Lbegin]:
                Lbegin +=1
            else:
                Lend -= 1
        return maxarea
A = Solution()
a = [1,8,6,2,5,4,8,3,7]
print(A.maxArea(a))

    