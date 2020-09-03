from typing import List
class Solution:
    def largerectangle(self,height:List[str])->int:
        stack = [-1]
        maxarea = 0
        for i in range(len(height)):
            while stack[-1]!= -1 and height[stack[-1]]>=height[i]:
                maxarea = max(maxarea,height[stack.pop()]*(i-stack[-1]-1))
            stack.append(i)
        while stack[-1] != -1:
            maxarea = max(maxarea,height[stack.pop()]*(len(height)-stack[-1]-1))
        return maxarea
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0
        dp = [0]*len(matrix[0])
        maxrectangle = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                dp[j] = dp[j]+1 if matrix[i][j] == '1' else 0
            maxrectangle = max(maxrectangle,self.largerectangle(dp))
        return maxrectangle
A = Solution()
a = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
print(A.maximalRectangle(a))