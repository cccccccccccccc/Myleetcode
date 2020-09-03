# time complexity = O(n) space complexity = O(1)
# F(i) = max{F(i-1)+a[i],0}  DP（dynamic programming 
# if tmpmax < 0 tmpmax = 0 turn to next index 
#  maxsum = max(tmpmax)
from typing import List
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if max(nums)<= 0:
            return max(nums)
        i = 0
        maxsum = 0
        tmpsum = 0
        for i in range(len(nums)):
            tmpsum = tmpsum+nums[i]
            if tmpsum < 0:
                tmpsum = 0
            elif tmpsum > maxsum:
                maxsum = tmpsum
        return maxsum
A = Solution()
a = [-2,1,-3,4,-1,2,1,-5,4]
b= [0,0,0,0]
c = [-1,-2,-3,-4,-1]
print(A.maxSubArray(c))   