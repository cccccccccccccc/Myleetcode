"""
timecomplexity = O(logn) spacecomplexity = O(1)
use binary search 
l r is nums maxleft and maxright index get the middle index  
iterate while l<r if m is target if not check compare nums[l] and nums[m] if nums[l]is less than nums[m] continue check nums[l] nums[m] and target 's relationship;
if nums[l] is larger than nums[m] continue check if nums[m] nums[r] and target'srelationship  find out who need to be shift to the new place and continue
if but the end still can not find the target return -1
"""
from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) <= 0:
            return -1
        l , r = 0, len(nums)
        while l < r:
            m = l + (r-l)//2
            if nums[m] == target:
                return m
            if nums[l] < nums[m]:
                if nums[l] <= target and nums[m] > target:
                    r = m
                else:
                    l = m + 1
            else:
                if nums[m] < target and nums[r-1] >= target:
                    l = m + 1
                else:
                    r = m
        return -1

A = Solution()
a = [4,5,6,7,0,1,2]
b = [3,1]

'''
print(A.search(a,1))
print(A.search(a,4))
print(A.search(a,17))
print(A.search(a,7))
print(A.search(a,0))
print(A.search(a,2))
print(A.search(a,3))
print(A.search(a,-1))

print(A.search(b,1))
'''
