from typing import List
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        indexstack = []
        indexstack.append(-1)
        maxarea = 0
        for i in range(len(heights)):
            while indexstack[-1] != -1 and heights[indexstack[-1]]>=heights[i]:
                maxarea = max(maxarea,heights[indexstack.pop()]*(i-indexstack[-1]-1))
            indexstack.append(i)
        while len(indexstack) != 1 :
            maxarea = max(maxarea,heights[indexstack.pop()]*(len(heights)-indexstack[-1]-1)) 
        return maxarea
A = Solution()
a = [2,1,5,6,2,3]
print(A.largestRectangleArea(a))