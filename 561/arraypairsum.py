from typing import List
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        minpairsum = 0
        for i in range(0,len(nums),2):
            minpairsum += nums[i]
        return minpairsum
A = Solution()
a = [1,4,2,3,6,5,7,8]
print(A.arrayPairSum(a))    


