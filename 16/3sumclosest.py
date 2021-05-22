"""
time complexity = O(n^2) space complexity = O(1)
sort nums
iterate element in nums
define left right = element+1, len(nums)-1
if tmpsum == targert 
if tmpsum better than answer
if tmpsum > target move right point
else move left point
"""
from typing import List
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        if len(nums)<3:
            return
        answer = float('inf')
        nums.sort()
        for tmp in range(len(nums)-2):
            l = tmp+1
            r = len(nums)-1
            while l<r:
                currentsum = nums[tmp]+nums[l]+nums[r]
                if currentsum == target:
                    return target
                elif abs(currentsum-target) < abs(answer-target):
                    answer = currentsum
                elif currentsum > target:
                    r-=1
                else:
                    l+=1
        return answer
A = Solution()
a = [-1,2,1,-4]
target = 1
print(A.threeSumClosest(a,target))